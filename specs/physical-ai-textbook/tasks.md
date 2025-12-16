# Tasks: AI-Native Textbook for Physical AI & Humanoid Robotics

**Input**: Design documents from `specs/physical-ai-textbook/`
**Prerequisites**: `plan.md`, `spec.md`

## Milestone 1: Core Textbook Setup & Deployment (User Story 1)

**Goal**: Get a basic Docusaurus site with placeholder content deployed to a public URL.

-   [ ] **T1.1 [US1]**: Initialize a new Docusaurus project in the `a_docusaurus_site/` directory.
-   [ ] **T1.2 [US1]**: Configure `a_docusaurus_site/docusaurus.config.ts` with the book's title ("Physical AI & Humanoid Robotics"), a basic navbar, and a footer.
-   [ ] **T1.3 [US1]**: Create placeholder markdown files inside `a_docusaurus_site/docs/` for each of the 13 weeks outlined in the course syllabus.
-   [ ] **T1.4 [US1]**: Configure the sidebar in `a_docusaurus_site/sidebars.ts` to reflect the 13-week structure.
-   [ ] **T1.5 [US1]**: Set up a GitHub Actions workflow (`.github/workflows/deploy.yml`) to automatically build and deploy the Docusaurus site to GitHub Pages on push to the `main` branch.
-   [ ] **T1.6 [US1]**: Write the full content for the first two weeks in the corresponding markdown files (`a_docusaurus_site/docs/week-1.md`, `a_docusaurus_site/docs/week-2.md`).

**Checkpoint**: A live Docusaurus website is accessible and shows the 13-week structure with content for the first two weeks.

---

## Milestone 2: RAG Chatbot Backend & Data Ingestion (User Story 2)

**Goal**: Build the FastAPI backend and the data pipeline to feed the textbook content into the vector database.

-   [ ] **T2.1 [US2]**: Initialize a new Python project with FastAPI in the `b_chatbot_api/` directory.
-   [ ] **T2.2 [US2]**: Set up Neon Serverless Postgres and Qdrant Cloud accounts and store credentials securely as environment variables.
-   [ ] **T2.3 [US2]**: Create the data ingestion script at `c_scripts/ingest.py`. This script should:
    -   Scan the `a_docusaurus_site/docs/` directory for markdown files.
    -   Chunk the text content appropriately.
    -   Use the OpenAI API to generate embeddings for each chunk.
    -   Upsert the chunks and their embeddings into a Qdrant collection.
-   [ ] **T2.4 [US2]**: Run the `ingest.py` script to populate the vector database with the initial content.
-   [ ] **T2.5 [US2]**: Implement the RAG pipeline logic in `b_chatbot_api/app/core/rag.py`. This will query Qdrant for relevant context and then call the OpenAI chat completions API with a grounded prompt.
-   [ ] **T2.6 [US2]**: Implement the `POST /api/chat` endpoint in `b_chatbot_api/app/api/chat.py`, using the RAG pipeline.
-   [ ] **T2.7 [US2]**: Create a `Dockerfile` for the FastAPI application.

**Checkpoint**: The FastAPI backend is running. Sending a `curl` request to `/api/chat` successfully returns a grounded answer from the LLM.

---

## Milestone 3: Frontend & Chatbot Integration (User Story 2)

**Goal**: Create the chatbot's user interface and connect it to the backend.

-   [ ] **T3.1 [US2]**: Create a new React component for the chatbot UI at `a_docusaurus_site/src/components/Chatbot/`. It should include a message display area, a text input, and a send button.
-   [ ] **T3.2 [US2]**: "Swizzle" the Docusaurus `Root` component to wrap the entire site with a provider that manages the chatbot's state (e.g., visibility, messages).
-   [ ] **T3.3 [US2]**: Add the `Chatbot` component and a floating action button to the layout to toggle its visibility.
-   [ ] **T3.4 [US2]**: Implement the frontend logic to call the `POST /api/chat` endpoint on the FastAPI backend and display the streamed response.
-   [ ] **T3.5 [US2]**: Add frontend logic to detect when a user has selected text on the page and include that `selected_text` in the API call to the backend.

**Checkpoint**: A user can click the chat button on the live site, ask a question, and get a response. Selecting text and asking a question also works as expected.

---

## Milestone 4: User Authentication (User Story 3 - Bonus)

**Goal**: Integrate user sign-up and login.

-   [ ] **T4.1 [US3]**: Integrate the `better-auth.com` React SDK/components into the Docusaurus site, adding "Login" and "Logout" buttons to the navbar.
-   [ ] **T4.2 [US3]**: Create a new page for user profiling that is shown only after the first successful login. This page will contain a form asking about the user's software and hardware background.
-   [ ] **T4.3 [US3]**: Create a `users` table in the Neon Postgres database with fields for `user_id` and `profile_data`.
-   [ ] **T4.4 [US3]**: Create a secure `POST /api/users/profile` endpoint in the FastAPI backend that takes the user's auth token and profile data and saves it to the database.
-   [ ] **T4.5 [US3]**: Connect the frontend profiling form to the backend endpoint.

**Checkpoint**: A user can sign up, log in, provide their background information, and their session is persisted.

---

## Milestone 5: Personalization & Translation (User Story 4 - Bonus)

**Goal**: Implement the dynamic content features for logged-in users.

-   [ ] **T5.1 [US4]**: Create a secure `POST /api/personalize` endpoint in FastAPI that receives content, gets the user's profile from the database, and calls the OpenAI API with instructions to tailor the content to that profile.
-   [ ] **T5.2 [US4]**: Create a secure `POST /api/translate` endpoint in FastAPI that calls the OpenAI API to translate given content to Urdu.
-   [ ] **T5.3 [US4]**: In the Docusaurus chapter component, add "Personalize" and "Translate" buttons that are only visible if a user is logged in.
-   [ ] **T5.4 [US4]**: Wire up the buttons to their respective backend endpoints and render the modified content that is returned.

**Checkpoint**: A logged-in user can click the "Personalize" or "Translate" buttons in a chapter and see the content update dynamically.
