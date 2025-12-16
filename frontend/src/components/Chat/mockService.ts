// Mock service for when backend is unavailable
export const mockResponses = {
  'what is this book about': 'This book is about Physical AI & Humanoid Robotics. It covers the fundamentals of embodied intelligence, robot control systems, AI applications in robotics, and how artificial intelligence can be integrated with physical systems for real-world applications.',
  'what is physical ai': 'Physical AI refers to artificial intelligence systems that interact with the physical world through robots and other embodied agents. It combines machine learning with physical interaction capabilities, focusing on how AI can understand and manipulate physical objects and environments.',
  'what is humanoid robotics': 'Humanoid robotics focuses on creating robots with human-like form and capabilities. This includes bipedal locomotion, manipulation, and human-robot interaction. The field explores how robots can move, act, and interact like humans.',
  'how does robot learning work': 'Robot learning involves training AI models that allow robots to adapt and improve their behavior based on experience. This includes reinforcement learning, imitation learning, and other techniques. Robots can learn from sensor data, environmental interactions, and human demonstrations.',
  'what is embodied intelligence': 'Embodied intelligence is the concept that intelligence emerges from the interaction between an agent and its environment. It emphasizes that physical form and environment are crucial for intelligence, rather than intelligence being purely computational.',
  'what are the main topics': 'The main topics include: 1) Introduction to Physical AI, 2) Humanoid Robot Design, 3) Control Systems for Robotics, 4) Sensing and Perception for Robots, 5) Robot Learning and Adaptation, 6) Human-Robot Interaction, 7) Applications of Physical AI.',
  'what is the difference between ai and physical ai': 'Traditional AI focuses on computational intelligence and data processing, while Physical AI emphasizes the integration of AI with physical systems. Physical AI considers how intelligence is shaped by physical embodiment, sensorimotor interactions, and environmental constraints.',
  'what is reinforcement learning for robots': 'Reinforcement learning in robotics is a method where robots learn optimal behaviors through trial and error, receiving rewards for desirable actions. This approach is particularly powerful for teaching robots complex tasks like walking, manipulation, and navigation in physical environments.',
  'how do robots perceive their environment': 'Robots perceive their environment through various sensors including cameras, lidar, ultrasonic sensors, and tactile sensors. These sensors collect data that is processed by perception algorithms to understand the robot\'s surroundings, identify objects, and navigate safely.',
  'what is robot path planning': 'Robot path planning is the process of determining a safe and efficient route for a robot to move from its current location to a goal location. This involves considering obstacles, the robot\'s physical constraints, and environmental conditions.',
  'how do humanoid robots maintain balance': 'Humanoid robots maintain balance using control algorithms that process data from sensors like gyroscopes, accelerometers, and force/torque sensors. Advanced control techniques like the Zero Moment Point (ZMP) and Linear Inverted Pendulum models help maintain stability during walking and standing.',
  'what is computer vision for robotics': 'Computer vision for robotics involves processing images and video to enable robots to recognize objects, navigate environments, and interact with physical objects. It includes object detection, tracking, 3D reconstruction, and scene understanding.',
  'what are the challenges in robotics': 'Key challenges include robust perception in dynamic environments, real-time processing for control, energy efficiency, safety, and developing systems that can adapt to novel situations. Integration of multiple complex subsystems is also challenging.',
  'default': 'Hello! I am your AI assistant for the Physical AI & Humanoid Robotics textbook. I am here to help you understand concepts related to robot learning, control systems, computer vision, human-robot interaction, and other relevant topics. Please feel free to ask any questions you may have about the material.'
};

export async function getMockResponse(message: string): Promise<string> {
  // Convert message to lowercase for case-insensitive matching
  const lowerMsg = message.toLowerCase().trim();

  // Check for exact matches first
  for (const [key, response] of Object.entries(mockResponses)) {
    if (key === 'default') continue; // Skip the default case for exact matching

    if (lowerMsg === key) {
      return response;
    }
  }

  // Check for partial matches
  for (const [key, response] of Object.entries(mockResponses)) {
    if (key === 'default') continue; // Skip the default case for partial matching

    if (lowerMsg.includes(key) || key.includes(lowerMsg.split(' ')[0])) {
      return response;
    }
  }

  // If no specific match found, use the default
  return mockResponses.default;
}

export async function chatWithMockBackend(message: string): Promise<{response: string, session_id: string}> {
  // Simulate network delay
  await new Promise(resolve => setTimeout(resolve, 500 + Math.random() * 1000));

  const response = await getMockResponse(message);
  return {
    response,
    session_id: 'mock-session-' + Date.now().toString()
  };
}