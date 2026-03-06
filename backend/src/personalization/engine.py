# backend/src/personalization/engine.py
# Content personalization engine based on user background

from typing import Dict, List, Any
import re
from ..auth.models import User

class PersonalizationEngine:
    """
    Personalizes textbook content based on user's hardware/software background
    """
    
    # Complexity levels mapping
    COMPLEXITY_LEVELS = {
        "beginner": 1,
        "intermediate": 2, 
        "expert": 3
    }
    
    # Content modification strategies based on user background
    MODIFICATION_STRATEGIES = {
        "beginner": {
            "add_context": True,
            "simplify_equations": True,
            "add_examples": True,
            "expand_abbreviations": True
        },
        "intermediate": {
            "add_context": True,
            "simplify_equations": False,
            "add_examples": True,
            "expand_abbreviations": False
        },
        "expert": {
            "add_context": False,
            "simplify_equations": False,
            "add_examples": False,
            "expand_abbreviations": False
        }
    }
    
    # Field-specific content modifications
    FIELD_MODIFICATIONS = {
        "robotics": {
            "keywords": ["control", "motion", "kinematics", "dynamics"],
            "examples": "Robotic arm control example: Consider a 6-DOF robotic manipulator where each joint needs precise position control..."
        },
        "ai": {
            "keywords": ["learning", "neural", "algorithm", "optimization"],
            "examples": "AI application: In humanoid robotics, neural networks are used to learn walking patterns..."
        },
        "control_systems": {
            "keywords": ["feedback", "stability", "pid", "transfer function"],
            "examples": "Control theory application: PID controllers are used to maintain balance in bipedal robots..."
        },
        "embedded_systems": {
            "keywords": ["microcontroller", "real-time", "sensor", "actuator"],
            "examples": "Embedded implementation: Real-time constraints require careful timing for sensor fusion in humanoid robots..."
        }
    }
    
    @staticmethod
    def personalize_content(content: str, user: User) -> str:
        """
        Main method to personalize content based on user profile
        """
        # Get modification strategy based on software experience
        strategy = PersonalizationEngine.MODIFICATION_STRATEGIES.get(
            user.software_experience, 
            PersonalizationEngine.MODIFICATION_STRATEGIES["beginner"]
        )
        
        # Apply modifications based on strategy
        personalized_content = content
        
        # Add context for beginners
        if strategy["add_context"]:
            personalized_content = PersonalizationEngine._add_context(personalized_content, user)
        
        # Simplify equations for beginners
        if strategy["simplify_equations"]:
            personalized_content = PersonalizationEngine._simplify_equations(personalized_content)
        
        # Add examples based on user's field of interest
        if strategy["add_examples"]:
            personalized_content = PersonalizationEngine._add_field_examples(
                personalized_content, 
                user.field_of_interest
            )
        
        # Expand abbreviations for beginners
        if strategy["expand_abbreviations"]:
            personalized_content = PersonalizationEngine._expand_abbreviations(personalized_content)
        
        return personalized_content
    
    @staticmethod
    def _add_context(content: str, user: User) -> str:
        """
        Add context explanations based on user background
        """
        # Add explanations for complex concepts
        context_additions = []
        
        # Add explanations based on hardware experience
        if user.hardware_experience in ["none", "basic"]:
            # Add more hardware explanations
            content = re.sub(
                r'\b(SoC|FPGA|ASIC|MCU|SoM|PCB|ADC|DAC|PWM|UART|SPI|I2C|GPIO)\b',
                r'[\1 - System-on-Chip/Field-Programmable Gate Array/Application-Specific Integrated Circuit/Microcontroller Unit/System-on-Module/Printed Circuit Board/Analog-to-Digital Converter/Digital-to-Analog Converter/Pulse Width Modulation/Universal Asynchronous Receiver-Transmitter/Serial Peripheral Interface/Inter-Integrated Circuit/General Purpose Input/Output]',
                content
            )
        
        # Add explanations based on software experience
        if user.software_experience in ["beginner"]:
            # Add more software explanations
            content = re.sub(
                r'\b(API|SDK|IDE|RTOS|HAL|Firmware|Bootloader|Kernel|Driver|Framework|Library)\b',
                r'[\1 - Application Programming Interface/Software Development Kit/Integrated Development Environment/Real-Time Operating System/Hardware Abstraction Layer/Firmware/Bootloader/Kernel/Driver/Framework/Library]',
                content
            )
        
        return content
    
    @staticmethod
    def _simplify_equations(content: str) -> str:
        """
        Simplify complex equations for beginners
        """
        # Add step-by-step explanations for complex equations
        # Example: Add descriptive text around equations
        content = re.sub(
            r'(\$\$.*?\$\$)',  # Find LaTeX equations
            r'Equation: \1. This equation represents [simplified explanation for beginners]',
            content,
            flags=re.DOTALL
        )
        
        return content
    
    @staticmethod
    def _add_field_examples(content: str, field_of_interest: str) -> str:
        """
        Add examples relevant to user's field of interest
        """
        if field_of_interest in PersonalizationEngine.FIELD_MODIFICATIONS:
            field_info = PersonalizationEngine.FIELD_MODIFICATIONS[field_of_interest]
            example_text = field_info["examples"]
            
            # Add field-specific examples at the beginning of content
            content = f"**{field_info['keywords'][0].title()} Application:**\n{example_text}\n\n{content}"
        
        return content
    
    @staticmethod
    def _expand_abbreviations(content: str) -> str:
        """
        Expand technical abbreviations for beginners
        """
        # Common abbreviations in robotics and AI
        abbreviations = {
            "AI": "Artificial Intelligence",
            "ML": "Machine Learning",
            "NN": "Neural Network",
            "RNN": "Recurrent Neural Network",
            "CNN": "Convolutional Neural Network",
            "PID": "Proportional-Integral-Derivative",
            "DOF": "Degrees of Freedom",
            "URDF": "Unified Robot Description Format",
            "ROS": "Robot Operating System"
        }
        
        for abbr, full in abbreviations.items():
            content = re.sub(
                rf'\b({abbr})\b',
                f"{full} ({abbr})",
                content
            )
        
        return content

# Usage example:
# engine = PersonalizationEngine()
# personalized_content = engine.personalize_content(original_content, user_profile)