# Implementation Plan: AI-Native Textbook for Physical AI & Humanoid Robotics

**Branch**: `feat/physical-ai-textbook` | **Date**: 2025-12-09 | **Spec**: [specs/physical-ai-textbook/spec.md](specs/physical-ai-textbook/spec.md)
**Input**: Feature specification from `specs/physical-ai-textbook/spec.md`

## 1. Summary

This plan outlines the architecture and implementation strategy for creating an AI-native textbook on "Physical AI & Humanoid Robotics." The project involves two main components: a Docusaurus-based website for the textbook content and a FastAPI-powered RAG (Retrieval-Augmented Generation) chatbot integrated into the site. The plan also covers the architecture for optional bonus features, including user authentication, content personalization, and translation.

## 2. Scope and Dependencies

### In Scope
-   **Core Textbook:** Creation of content for all specified modules and deployment via Docusaurus on GitHub Pages/Vercel.
-   **RAG Chatbot:** A FastAPI backend providing a chat API, integrated with OpenAI, Qdrant, and Neon Postgres, and embedded as a component in the Docusaurus site.
-   **Bonus Features:** Implementation of user authentication (`better-auth.com`), content personalization, and Urdu translation as defined in the spec.

### Out of Scope
-   Development of a novel Large Language Model (LLM).
-   Procurement or programming of physical robot hardware.
-   Any features not explicitly mentioned in the project specification.

### Dependencies
-   **Services:** OpenAI API, Qdrant Cloud, Neon Serverless Postgres, `better-auth.com`.
-   **Frameworks:** Docusaurus (Node.js/React), FastAPI (Python).
-   **Tooling:** Spec-Kit Plus, Claude Code.

## 3. Key Architectural Decisions

-   **Frontend:** Docusaurus will be used as mandated. It provides an excellent, markdown-driven foundation for a technical book and is built on React, allowing for the integration of custom components like the chatbot.
-   **Backend (Chatbot & Services):** FastAPI is mandated and will be used to create the API endpoints for the chatbot, personalization, and translation. Its speed and modern Python features make it ideal for this.
-   **Repository Structure:** A monorepo structure will be adopted for simplicity. This will keep the frontend and backend code in a single GitHub repository, which is easier to manage for a solo developer in a hackathon context.
-   **Deployment Strategy:**
    -   The Docusaurus frontend will be deployed as a static site using GitHub Actions to GitHub Pages.
    -   The FastAPI backend will be containerized using Docker and deployed to a serverless platform that supports containers, such as Fly.io or Vercel Serverless Functions. This separates the stateful API from the static frontend.

📋 **Architectural decision detected:** The choice of a monorepo structure and a split deployment model (static frontend, containerized backend) is a significant architectural decision. To document the reasoning, run `/sp.adr "Monorepo and Split Deployment Strategy"`.

## 4. Project Structure

A single repository will be used, with a structure that separates the frontend and backend concerns.

```text
# Web application (frontend + backend)
.
├── a_docusaurus_site/   # Docusaurus project root
│   ├── blog/
│   ├── docs/          # Textbook content will go here
│   ├── src/
│   │   ├── components/
│   │   │   └── Chatbot/ # React component for the chatbot UI
│   │   └── pages/
│   ├── static/
│   └── docusaurus.config.ts
│
├── b_chatbot_api/        # FastAPI project root
│   ├── app/
│   │   ├── api/         # API endpoints (chat, personalize, translate)
│   │   ├── core/        # Core logic (embedding, RAG pipeline)
│   │   ├── models/      # Pydantic models
│   │   └── services/    # Services for OpenAI, Qdrant, etc.
│   ├── tests/
│   └── Dockerfile
│
└── c_scripts/
    └──-ingest.py     # Script to process markdown, create embeddings, and load into Qdrant

```

**Structure Decision**: A monorepo containing two main directories: `a_docusaurus_site` for the Docusaurus frontend and `b_chatbot_api` for the FastAPI backend. A top-level `c_scripts` directory will house standalone scripts, such as the data ingestion script for the vector database.

## 5. Interfaces and API Contracts

The FastAPI backend will expose the following endpoints:

-   `POST /api/chat`
    -   **Description**: Handles chat requests.
    -   **Request Body**: `{ "query": "string", "selected_text": "string" | null }`
    -   **Response Body**: `{ "answer": "string" }`
-   `POST /api/personalize` (Requires Auth)
    -   **Description**: Personalizes a given piece of content.
    -   **Request Body**: `{ "content": "string" }`
    -   **Response Body**: `{ "personalized_content": "string" }`
-   `POST /api/translate` (Requires Auth)
    -   **Description**: Translates content to Urdu.
    -   **Request Body**: `{ "content": "string" }`
    -   **Response Body**: `{ "translated_content": "string" }`

## 6. Data Management

-   **Textbook Content**: Stored as `.md` / `.mdx` files in the `a_docusaurus_site/docs/` directory.
-   **Vector Embeddings**: The `c_scripts/ingest.py` script will read all markdown files, chunk them, generate embeddings via the OpenAI API, and store them in the designated Qdrant Cloud collection. This script must be run whenever the book content is updated significantly.
-   **User Profiles**: A `users` table will be created in the Neon Postgres database to store a user's ID (from `better-auth.com`) and their self-reported hardware/software background.

## 7. Risk Analysis and Mitigation

-   **Risk**: High latency from external API calls (OpenAI) in the chat function.
    -   **Mitigation**: Implement streaming responses from the FastAPI backend to the frontend. This will display the answer token-by-token, improving perceived performance.
-   **Risk**: Ensuring the RAG pipeline is grounded and does not hallucinate.
    -   **Mitigation**: Engineer prompts carefully to instruct the LLM to only use the provided context from the vector search. Implement a fallback response like "I cannot answer that based on the provided text."
-   **Risk**: Scope management for bonus features within the hackathon timeline.
    -   **Mitigation**: Prioritize the P1 user stories (core textbook and chatbot) first. Timebox the development of each bonus feature, starting with authentication, which is a prerequisite for the others.

## 8. Evaluation and Validation

-   **Unit & Integration Tests**: `pytest` will be used for the FastAPI backend, and Jest/React Testing Library for the Docusaurus components.
-   **Manual Testing**: Follow the acceptance criteria for each user story in the `spec.md` file.
-   **Performance**: Use Lighthouse to measure the performance of the deployed Docusaurus site.
-   **Final Deliverables**: The project will be considered complete when all items on the submission checklist (GitHub repo, deployed link, video) are ready.
