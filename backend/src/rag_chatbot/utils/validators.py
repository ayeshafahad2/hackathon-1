import re
from typing import Optional


class Validators:
    @staticmethod
    def validate_message_content(content: str) -> bool:
        """
        Validate that the message content is appropriate for processing
        """
        if not content or len(content.strip()) == 0:
            return False

        # Check for minimum length
        if len(content.strip()) < 1:
            return False

        # Check for maximum length
        if len(content) > 2000:  # As defined in the request model
            return False

        return True

    @staticmethod
    def validate_language_code(language: str) -> bool:
        """
        Validate that the language code is supported
        """
        supported_languages = ["en", "ur"]  # English and Urdu as per spec
        return language.lower() in supported_languages

    @staticmethod
    def validate_session_id(session_id: str) -> bool:
        """
        Validate session ID format
        """
        if not session_id:
            return False

        # Basic UUID validation (simplified)
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE
        )
        return bool(uuid_pattern.match(session_id))

    @staticmethod
    def sanitize_input(text: str) -> str:
        """
        Sanitize input text to prevent injection attacks
        """
        if not text:
            return ""

        # Remove potentially dangerous characters/sequences
        # In a production environment, use a more comprehensive sanitization
        sanitized = text.replace('\0', '')  # Remove null bytes
        return sanitized

    @staticmethod
    def validate_selected_text(selected_text: Optional[str]) -> bool:
        """
        Validate selected text parameter
        """
        if selected_text is None:
            return True

        if len(selected_text) > 5000:  # Set a reasonable limit for selected text
            return False

        return True