from fastapi import FastAPI, Depends, HTTPException, status, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional, List
import sqlite3
import json

# ================= CONFIG =================
SECRET_KEY = "SUPER_SECRET_KEY_CHANGE_ME"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

# =========================================
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# ================= DATABASE SETUP =================
# Initialize an in-memory SQLite database for demo purposes
# In production, you would use a persistent database
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    # Create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            software_experience TEXT DEFAULT 'beginner',
            hardware_experience TEXT DEFAULT 'none',
            programming_languages TEXT DEFAULT '[]',  -- JSON string
            field_of_interest TEXT DEFAULT '',
            educational_affiliation TEXT DEFAULT '',
            personalization_enabled BOOLEAN DEFAULT 0,
            bonus_points INTEGER DEFAULT 0,
            profile_complete BOOLEAN DEFAULT 0
        )
    ''')
    
    # Create a default user if none exists
    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] == 0:
        default_hashed = pwd_context.hash("password123")
        c.execute('''
            INSERT INTO users 
            (email, hashed_password, software_experience, hardware_experience) 
            VALUES (?, ?, ?, ?)
        ''', ("test@example.com", default_hashed, "beginner", "none"))
    
    conn.commit()
    conn.close()

# Initialize database
init_db()

# ================= MODELS =================
class LoginRequest(BaseModel):
    email: str
    password: str

class UserCreateRequest(BaseModel):
    email: str
    password: str
    software_experience: Optional[str] = "beginner"
    hardware_experience: Optional[str] = "none"
    programming_languages: Optional[List[str]] = []
    field_of_interest: Optional[str] = ""
    educational_affiliation: Optional[str] = ""

class Token(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: int
    email: str
    software_experience: str
    hardware_experience: str
    programming_languages: List[str]
    field_of_interest: str
    educational_affiliation: str
    personalization_enabled: bool
    bonus_points: int
    profile_complete: bool

# ================= HELPERS =================
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_by_email(email: str):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = c.fetchone()
    conn.close()
    
    if row:
        return {
            'id': row[0],
            'email': row[1],
            'hashed_password': row[2],
            'software_experience': row[3],
            'hardware_experience': row[4],
            'programming_languages': json.loads(row[5]),
            'field_of_interest': row[6],
            'educational_affiliation': row[7],
            'personalization_enabled': bool(row[8]),
            'bonus_points': row[9],
            'profile_complete': bool(row[10])
        }
    return None

def create_user(user_data: UserCreateRequest):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    try:
        c.execute('''
            INSERT INTO users 
            (email, hashed_password, software_experience, hardware_experience, 
             programming_languages, field_of_interest, educational_affiliation, profile_complete)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_data.email,
            get_password_hash(user_data.password),
            user_data.software_experience,
            user_data.hardware_experience,
            json.dumps(user_data.programming_languages),
            user_data.field_of_interest,
            user_data.educational_affiliation,
            True if user_data.software_experience != "beginner" or user_data.hardware_experience != "none" else False
        ))
        user_id = c.lastrowid
        conn.commit()
        conn.close()
        
        return get_user_by_email(user_data.email)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already registered")

def update_user_bonus_points(user_id: int, points: int):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    c.execute("UPDATE users SET bonus_points = bonus_points + ? WHERE id = ?", (points, user_id))
    conn.commit()
    conn.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = get_user_by_email(email)
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ================= ROUTES =================
@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/v1/auth/login", response_model=Token)
def login(data: LoginRequest):
    user = get_user_by_email(data.email)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(data.password, user['hashed_password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": data.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.post("/api/v1/auth/register", response_model=Token)
def register(data: UserCreateRequest):
    # Check if user already exists
    existing_user = get_user_by_email(data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    user = create_user(data)
    
    # Create access token
    access_token = create_access_token(
        data={"sub": data.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@app.get("/api/v1/auth/me", response_model=UserResponse)
def get_current_user_profile(user=Depends(get_current_user)):
    return user

@app.put("/api/v1/auth/profile", response_model=UserResponse)
def update_profile(
    software_experience: Optional[str] = Body(None),
    hardware_experience: Optional[str] = Body(None),
    programming_languages: Optional[List[str]] = Body(None),
    field_of_interest: Optional[str] = Body(None),
    educational_affiliation: Optional[str] = Body(None),
    user=Depends(get_current_user)
):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    # Build the update query dynamically based on provided parameters
    updates = []
    params = []
    
    if software_experience is not None:
        updates.append("software_experience = ?")
        params.append(software_experience)
        
    if hardware_experience is not None:
        updates.append("hardware_experience = ?")
        params.append(hardware_experience)
        
    if programming_languages is not None:
        updates.append("programming_languages = ?")
        params.append(json.dumps(programming_languages))
        
    if field_of_interest is not None:
        updates.append("field_of_interest = ?")
        params.append(field_of_interest)
        
    if educational_affiliation is not None:
        updates.append("educational_affiliation = ?")
        params.append(educational_affiliation)
    
    if updates:
        query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
        params.append(user['id'])
        c.execute(query, params)
        conn.commit()
    
    conn.close()
    
    # Return updated user
    updated_user = get_user_by_email(user['email'])
    return updated_user



