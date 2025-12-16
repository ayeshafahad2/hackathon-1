import re
from typing import List
from ..models.data_models import Document


class TextProcessor:
    @staticmethod
    def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
        """
        Split text into overlapping chunks for better context retrieval
        """
        if len(text) <= chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size

            # If we're near the end, just take the remaining text
            if end >= len(text):
                chunks.append(text[start:])
                break

            # Try to break at sentence boundary
            chunk = text[start:end]
            last_period = chunk.rfind('.')
            last_exclamation = chunk.rfind('!')
            last_question = chunk.rfind('?')
            last_space = chunk.rfind(' ')

            # Find the best break point
            break_point = max(last_period, last_exclamation, last_question)
            if break_point == -1:
                break_point = last_space

            if break_point != -1 and break_point > len(chunk) // 2:  # Only if break point is in the second half
                actual_end = start + break_point + 1
                chunks.append(text[start:actual_end])
                start = actual_end - overlap
            else:
                # If no good break point found, just take the chunk
                chunks.append(text[start:end])
                start = end - overlap

        return chunks

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean text by removing extra whitespace and normalizing
        """
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove extra newlines but preserve paragraph structure
        text = re.sub(r'\n\s*\n', '\n\n', text)
        return text.strip()

    @staticmethod
    def create_documents_from_text(text: str, source_metadata: dict = None) -> List[Document]:
        """
        Create Document objects from text, chunking as necessary
        """
        if source_metadata is None:
            source_metadata = {}

        # Clean the text first
        cleaned_text = TextProcessor.clean_text(text)

        # Chunk the text
        chunks = TextProcessor.chunk_text(cleaned_text)

        documents = []
        for i, chunk in enumerate(chunks):
            doc_id = f"{source_metadata.get('source_id', 'unknown')}_{i}" if source_metadata.get('source_id') else f"chunk_{i}_{hash(chunk) % 10000}"

            metadata = source_metadata.copy()
            metadata['chunk_index'] = i
            metadata['total_chunks'] = len(chunks)

            doc = Document(
                id=doc_id,
                content=chunk,
                metadata=metadata
            )
            documents.append(doc)

        return documents

    @staticmethod
    def extract_key_sentences(text: str, num_sentences: int = 3) -> List[str]:
        """
        Extract key sentences from text (simplified approach)
        """
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        # For now, just return the first few sentences
        # In a more advanced implementation, we could use NLP techniques
        return sentences[:num_sentences] if len(sentences) >= num_sentences else sentences