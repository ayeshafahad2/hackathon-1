from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="RAG Chatbot API",
    description="Physical AI & Humanoid Robotics Textbook Chatbot",
    version="1.0.0"
)

# Add CORS middleware - allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "RAG Chatbot API is running",
        "version": "1.0.0",
        "status": "healthy"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "RAG Chatbot",
        "content_loaded": True,
        "backend": "Hugging Face Spaces"
    }

@app.post("/api/v1/chat")
def chat(message: dict):
    """Simple chat endpoint with mock response"""
    user_message = message.get("message", "").lower()
    
    # Simple keyword-based responses
    if "physical ai" in user_message or "physical artificial intelligence" in user_message:
        response = """**Physical AI**

Physical AI represents a paradigm shift in artificial intelligence, moving beyond purely digital computations to systems that interact with and understand the physical world.

**Key Insights:**
• **Embodiment**: Intelligence is intertwined with physical body and environment
• **Perception-Action Cycle**: Robots perceive environment and use information to inform actions
• **Real-World Constraints**: Must handle uncertainty, noise, and physics

**Related Concepts:**
→ Embodied Intelligence
→ Sensorimotor Contingencies
→ Humanoid Robotics

📖 *Introduction to Physical AI* → *Foundations of Physical AI*"""
    elif "humanoid" in user_message:
        response = """**Humanoid Robots**

Humanoid robots are designed to mimic the human form, offering unique advantages for human environments.

**Key Insights:**
• **Anthropomorphic Design**: Body structure similar to humans
• **Bipedal Locomotion**: Walk on two legs with sophisticated balance
• **Applications**: Healthcare, manufacturing, service industry, research

**Related Concepts:**
→ Bipedal Walking
→ Human-Robot Interaction
→ Robot Kinematics

📖 *Introduction to Physical AI* → *Overview of Humanoid Robotics*"""
    elif "ros" in user_message or "ros 2" in user_message:
        response = """**ROS 2 (Robot Operating System 2)**

ROS 2 is a flexible framework for writing robot software with distributed, peer-to-peer architecture.

**Key Insights:**
• **Nodes**: Executable processes performing specific tasks
• **Topics**: Publish-subscribe communication for streaming data
• **Services**: Synchronous request-reply communication
• **Actions**: Long-running tasks with feedback

**Related Concepts:**
→ Robot Middleware
→ rclpy (Python client)
→ URDF (Robot Description)

📖 *ROS 2 Fundamentals* → *Architecture and Core Concepts*"""
    elif "zmp" in user_message or "zero moment point" in user_message:
        response = """**Zero Moment Point (ZMP)**

ZMP is the key concept for stable bipedal walking in humanoid robots.

**Key Insights:**
• **Definition**: Point where net moment of inertial and gravitational forces is zero
• **Stability**: ZMP must stay within support polygon (area under feet)
• **Control**: Used for gait generation and balance control

**Related Concepts:**
→ Center of Mass (CoM)
→ Support Polygon
→ Bipedal Locomotion

📖 *Humanoid Kinematics* → *Bipedal Locomotion and Balance*"""
    elif "gazebo" in user_message or "simulation" in user_message:
        response = """**Gazebo Simulation**

Gazebo is a powerful 3D robotics simulator for testing algorithms and designing robots.

**Key Insights:**
• **Physics Engines**: ODE, Bullet, DART, Newton (GPU-accelerated)
• **Sensor Simulation**: LiDAR, cameras, IMUs, force sensors
• **ROS 2 Integration**: Seamless bridge with ROS 2 ecosystem

**Related Concepts:**
→ Digital Twin
→ URDF/SDF Formats
→ Sim-to-Real Transfer

📖 *Robot Simulation* → *Gazebo Environment Setup*"""
    elif "nvidia" in user_message or "isaac" in user_message:
        response = """**NVIDIA Isaac Platform**

NVIDIA Isaac provides AI-powered robot development tools with simulation and perception.

**Key Insights:**
• **Isaac Sim**: Photorealistic simulation on Omniverse
• **Isaac Lab**: Reinforcement learning framework
• **Synthetic Data**: Auto-labeled training data generation
• **Hardware Acceleration**: GPU-optimized perception pipelines

**Related Concepts:**
→ Sim-to-Real Transfer
→ Reinforcement Learning
→ Foundation Models

📖 *NVIDIA Isaac Platform* → *Isaac Sim Overview*"""
    else:
        response = f"""**Question Received:** {message.get("message", "")}

I'm a RAG chatbot for the Physical AI & Humanoid Robotics textbook. I can help you understand concepts from the course.

**Try asking about:**
• Physical AI and embodied intelligence
• Humanoid robots and their design
• ROS 2 middleware and control
• Kinematics and bipedal walking (ZMP)
• Gazebo simulation
• NVIDIA Isaac platform
• Vision-Language-Action models

📖 *Textbook Chatbot* → *Ready to Help*"""
    
    return {
        "response": response,
        "sources": [{"chapter": "Textbook", "section": "RAG Response", "similarity": 0.95}],
        "session_id": "session-123",
        "confidence": 0.95,
        "language": "en"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
