# Project Constitution: Physical AI & Humanoid Robotics Textbook

## 1. Mission

Our primary mission is to create a comprehensive, AI-native textbook for the "Physical AI & Humanoid Robotics" course. This project is a cornerstone of Panaversity's initiative to build a portal for AI-driven technical education, empowering authors and learners alike. We aim to produce a cutting-edge educational resource that bridges the gap between digital AI and physical, embodied intelligence.

## 2. Core Deliverables

The project is defined by two core deliverables that constitute the base functionality.

### 2.1. AI/Spec-Driven Book Creation
- **Content:** An educational textbook on "Physical AI & Humanoid Robotics".
- **Methodology:** The book will be written using a Spec-Driven Development (SDD) approach, facilitated by Spec-Kit Plus.
- **Tooling:**
    - **Framework:** Docusaurus
    - **AI Assistant:** Claude Code
    - **Process Management:** Spec-Kit Plus
- **Deployment:** The final book will be deployed and accessible via GitHub Pages or Vercel.

### 2.2. Integrated RAG Chatbot
- **Functionality:** A Retrieval-Augmented Generation (RAG) chatbot will be embedded within the book. The chatbot must be capable of:
    - Answering user questions based on the book's entire content.
    - Answering questions based on specific text selected by the user.
- **Technology Stack:**
    - **Backend:** FastAPI
    - **Database:** Neon Serverless Postgres
    - **Vector Store:** Qdrant Cloud (Free Tier)
    - **AI/SDKs:** OpenAI Agents/ChatKit SDKs

## 3. Bonus Objectives

To push the boundaries of AI-native education, participants can earn bonus points by implementing the following features:

- **Reusable Intelligence (50 Points):** Create and utilize reusable intelligence through Claude Code Subagents and Agent Skills.
- **Authentication & Personalization (50 Points):** Implement user Signup and Sign-in using `better-auth.com`. During signup, collect user's software and hardware background to enable personalized content delivery.
- **Dynamic Content Personalization (50 Points):** Allow logged-in users to personalize the content within chapters at the click of a button.
- **Translation (50 Points):** Enable logged-in users to translate chapter content into Urdu with a button press.

## 4. Technical and Course Blueprint

### 4.1. Course Structure
The textbook will be structured around the following modules:
- **Module 1: The Robotic Nervous System (ROS 2):** Middleware for robot control.
- **Module 2: The Digital Twin (Gazebo & Unity):** Physics simulation and environment building.
- **Module 3: The AI-Robot Brain (NVIDIA Isaac™):** Advanced perception and training.
- **Module 4: Vision-Language-Action (VLA):** The convergence of LLMs and Robotics.

### 4.2. Hardware & Architectural Considerations
The content must be written with a deep understanding of the demanding hardware requirements for Physical AI. The textbook should provide clear guidance on setting up development environments, whether using:
- **On-Premise Labs:** High-performance workstations with NVIDIA RTX GPUs and dedicated Edge AI kits (e.g., NVIDIA Jetson Orin).
- **Cloud-Native Labs:** Utilizing cloud instances (e.g., AWS/Azure) for simulation and local "bridge" hardware for physical deployment.
The architecture must address the "Latency Trap" by training models in the cloud and deploying them to local edge devices.

## 5. Project Management & Timeline

- **Process:** Adherence to Spec-Driven Development (SDD) is mandatory. All work will be tracked and documented using PHRs (Prompt History Records) and ADRs (Architectural Decision Records) as appropriate.
- **Submission Deadline:** Sunday, November 30, 2025, at 06:00 PM.
- **Deliverables for Submission:**
    1. Public GitHub Repository Link.
    2. Published Book Link (GitHub Pages or Vercel).
    3. A demo video (under 90 seconds).