# Welcome to Physical AI & Humanoid Robotics

This AI-native textbook is designed for an intensive course in **Physical AI & Humanoid Robotics**, bridging the critical gap between artificial intelligence in digital domains and its manifestation in the physical world. As we stand at the precipice of a new era where intelligent agents and humanoid robots will partner with humans in various facets of life and work, the demand for new, specialized skills is paramount. This course, and by extension this textbook, aims to equip students with the knowledge and practical expertise to design, simulate, and deploy humanoid robots capable of natural human interactions.

## Course Overview: AI Systems in the Physical World. Embodied Intelligence.

The future of AI extends beyond digital spaces into the physical world. This capstone quarter introduces Physical AI—AI systems that function in reality and comprehend physical laws. Students learn to design, simulate, and deploy humanoid robots capable of natural human interactions using ROS 2, Gazebo, and NVIDIA Isaac. The course is structured into four core modules:

### Module 1: The Robotic Nervous System (ROS 2)
Focus: Middleware for robot control.
- ROS 2 Nodes, Topics, and Services.
- Bridging Python Agents to ROS controllers using `rclpy`.
- Understanding URDF (Unified Robot Description Format) for humanoids.

### Module 2: The Digital Twin (Gazebo & Unity)
Focus: Physics simulation and environment building.
- Simulating physics, gravity, and collisions in Gazebo.
- High-fidelity rendering and human-robot interaction in Unity.
- Simulating sensors: LiDAR, Depth Cameras, and IMUs.

### Module 3: The AI-Robot Brain (NVIDIA Isaac™)
Focus: Advanced perception and training.
- NVIDIA Isaac Sim: Photorealistic simulation and synthetic data generation.
- Isaac ROS: Hardware-accelerated VSLAM (Visual SLAM) and navigation.
- Nav2: Path planning for bipedal humanoid movement.

### Module 4: Vision-Language-Action (VLA)
Focus: The convergence of LLMs and Robotics.
- Voice-to-Action: Using OpenAI Whisper for voice commands.
- Cognitive Planning: Using LLMs to translate natural language ("Clean the room") into a sequence of ROS 2 actions.
- Capstone Project: The Autonomous Humanoid. A final project where a simulated robot receives a voice command, plans a path, navigates obstacles, identifies an object using computer vision, and manipulates it.

## Why Physical AI Matters

Humanoid robots are poised to excel in our human-centered world because they share our physical form and can be trained with abundant data from interacting in human environments. This represents a significant transition from AI models confined to digital environments to embodied intelligence that operates in physical space.

## Learning Outcomes

Upon completion of this course, students will be able to:
- Understand Physical AI principles and embodied intelligence.
- Master ROS 2 (Robot Operating System) for robotic control.
- Simulate robots with Gazebo and Unity.
- Develop with NVIDIA Isaac AI robot platform.
- Design humanoid robots for natural interactions.
- Integrate GPT models for conversational robotics.

## Hardware Requirements

This course is technically demanding, sitting at the intersection of Physics Simulation (Isaac Sim/Gazebo), Visual Perception (SLAM/Computer Vision), and Generative AI (LLMs/VLA). For the capstone involving a "Simulated Humanoid," a primary investment in High-Performance Workstations is required. To fulfill the "Physical AI" promise, students also need Edge Computing Kits (brains without bodies) or specific robot hardware.

### 1. The "Digital Twin" Workstation (Required per Student)
- **GPU (The Bottleneck):** NVIDIA RTX 4070 Ti (12GB VRAM) or higher.
  - *Why:* High VRAM is essential for loading USD assets for robots and environments, plus running VLA models simultaneously.
  - *Ideal:* RTX 3090 or 4090 (24GB VRAM) for smoother "Sim-to-Real" training.
- **CPU:** Intel Core i7 (13th Gen+) or AMD Ryzen 9.
  - *Why:* Physics calculations (Rigid Body Dynamics) in Gazebo/Isaac are CPU-intensive.
- **RAM:** 64 GB DDR5 (32 GB is the absolute minimum, but may crash during complex scene rendering).
- **OS:** Ubuntu 22.04 LTS.
  - *Note:* While Isaac Sim runs on Windows, ROS 2 (Humble/Iron) is native to Linux. Dual-booting or dedicated Linux machines are mandatory for a friction-free experience.

### 2. The "Physical AI" Edge Kit
This kit covers Module 3 (Isaac ROS) and Module 4 (VLA).
- **The Brain:** NVIDIA Jetson Orin Nano (8GB) or Orin NX (16GB).
  - *Role:* Industry standard for embodied AI. Students deploy ROS 2 nodes here to understand resource constraints.
- **The Eyes (Vision):** Intel RealSense D435i or D455.
  - *Role:* Provides RGB and Depth data, essential for VSLAM and Perception modules.
- **The Inner Ear (Balance):** Generic USB IMU (BNO055).
- **Voice Interface:** A simple USB Microphone/Speaker array (e.g., ReSpeaker) for "Voice-to-Action" Whisper integration.

### 3. The Robot Lab (Optional, for Physical Deployment)
Options depend on budget:
- **Option A: The "Proxy" Approach (Recommended for Budget):** Use a quadruped (dog) or a robotic arm as a proxy.
  - *Example Robot:* Unitree Go2 Edu (~$1,800 - $3,000).
- **Option B: The "Miniature Humanoid" Approach:** Small, table-top humanoids.
  - *Examples:* Unitree G1 (~$16k) or Robotis OP3 (~$12k). Budget Alternative: Hiwonder TonyPi Pro (~$600).
- **Option C: The "Premium" Lab (Sim-to-Real specific):** For deploying the Capstone to a real humanoid.
  - *Example Robot:* Unitree G1 Humanoid.

### Summary of Architecture
To teach this successfully, your lab infrastructure should look like this:
-   **Sim Rig:** PC with RTX 4080 + Ubuntu 22.04. Runs Isaac Sim, Gazebo, Unity, and trains LLM/VLA models.
-   **Edge Brain:** Jetson Orin Nano. Runs the "Inference" stack. Students deploy their code here.
-   **Sensors:** RealSense Camera + Lidar. Connected to the Jetson to feed real-world data to the AI.
-   **Actuator:** Unitree Go2 or G1 (Shared). Receives motor commands from the Jetson.

## Assessments

Assessments will include:
-   ROS 2 package development project.
-   Gazebo simulation implementation.
-   Isaac-based perception pipeline.
-   Capstone: Simulated humanoid robot with conversational AI.
