"""
RAG Service for Textbook Chatbot
Combines retrieval and generation for answering questions
"""

import json
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path
import os

from .embedding_service import get_embedding_service
from .vector_store import get_vector_store
from .qwen_service import get_qwen_service

logger = logging.getLogger(__name__)

class RAGService:
    """Service for RAG-based question answering"""
    
    def __init__(self, content_path: Optional[str] = None):
        """
        Initialize the RAG service
        
        Args:
            content_path: Path to textbook content JSON file
        """
        self.embedding_service = get_embedding_service()
        self.vector_store = get_vector_store()
        self.qwen_service = get_qwen_service()
        self.content_path = content_path or self._get_default_content_path()
        self.content_loaded = False
        
    def _get_default_content_path(self) -> str:
        """Get default path to textbook content"""
        base_dir = Path(__file__).parent.parent
        return str(base_dir / "data" / "textbook_content.json")
    
    def load_content(self) -> Dict[str, Any]:
        """
        Load textbook content and populate vector store
        
        Returns:
            Dictionary with loading statistics
        """
        try:
            logger.info(f"Loading content from: {self.content_path}")
            
            with open(self.content_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Reset vector store
            self.vector_store.reset()
            
            # Process chapters and sections
            documents = []
            embeddings = []
            metadatas = []
            ids = []
            
            for chapter in data.get("chapters", []):
                chapter_id = chapter.get("id")
                chapter_title = chapter.get("title")
                chapter_order = chapter.get("order", 0)
                difficulty = chapter.get("difficulty", "Unknown")
                
                for section in chapter.get("sections", []):
                    section_id = section.get("id")
                    section_title = section.get("title")
                    content = section.get("content")
                    tags = section.get("tags", [])
                    metadata = section.get("metadata", {})
                    
                    # Create document with context
                    doc_text = f"""Chapter: {chapter_title}
Section: {section_title}
Content: {content}"""
                    
                    documents.append(doc_text)
                    ids.append(section_id)
                    # Convert all metadata values to strings for ChromaDB
                    safe_metadata = {}
                    for key, value in {
                        "chapter_id": chapter_id,
                        "chapter_title": chapter_title,
                        "chapter_order": chapter_order,
                        "section_id": section_id,
                        "section_title": section_title,
                        "difficulty": difficulty,
                        "tags": json.dumps(tags),
                        **metadata
                    }.items():
                        if isinstance(value, list):
                            safe_metadata[key] = json.dumps(value)
                        elif value is None:
                            safe_metadata[key] = ""
                        else:
                            safe_metadata[key] = str(value) if not isinstance(value, (str, int, float, bool)) else value
                    metadatas.append(safe_metadata)
            
            # Generate embeddings
            logger.info(f"Generating embeddings for {len(documents)} sections...")
            embeddings = self.embedding_service.embed_texts(documents)
            
            # Add to vector store
            logger.info("Adding documents to vector store...")
            self.vector_store.add_documents(
                documents=documents,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
            
            self.content_loaded = True
            stats = self.vector_store.get_collection_stats()
            
            logger.info(f"Content loaded successfully: {stats}")
            
            return {
                "success": True,
                "message": "Content loaded successfully",
                "stats": stats,
                "chapters_processed": len(data.get("chapters", []))
            }
            
        except Exception as e:
            logger.error(f"Error loading content: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def retrieve_context(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve relevant context for a query with improved matching
        """
        try:
            # Generate query embedding
            query_embedding = self.embedding_service.embed_text(query)
            
            # Search vector store with more results for better matching
            results = self.vector_store.search(
                query_embedding=query_embedding,
                n_results=n_results
            )
            
            # Format results - ChromaDB returns distances, convert to similarity
            context_list = []
            for i, (doc, metadata, distance) in enumerate(
                zip(
                    results["documents"],
                    results["metadatas"],
                    results["distances"]
                )
            ):
                # ChromaDB with cosine space: distance = 1 - similarity
                # So similarity = 1 - distance
                base_similarity = 1 - distance
                
                # Boost score if section title or content matches query keywords
                query_lower = query.lower()
                query_words = [w for w in query_lower.split() if len(w) > 2]
                
                section_title = metadata.get("section_title", "").lower()
                chapter_title = metadata.get("chapter_title", "").lower()
                tags_str = metadata.get("tags", "").lower()
                
                # Check for keyword match in section title, chapter, and tags
                for word in query_words:
                    # Fix common typos
                    corrected_word = word
                    if 'humaniod' in word:
                        corrected_word = 'humanoid'
                    elif 'robtics' in word:
                        corrected_word = 'robotics'
                    elif 'kinemtics' in word:
                        corrected_word = 'kinematics'
                    
                    # Strong boost for exact title match
                    if corrected_word in section_title:
                        base_similarity += 0.5
                    # Moderate boost for chapter title match
                    elif corrected_word in chapter_title:
                        base_similarity += 0.3
                    # Small boost for tags match
                    elif corrected_word in tags_str:
                        base_similarity += 0.2
                    
                    # Also check original word
                    if word in section_title or word in chapter_title or word in tags_str:
                        base_similarity += 0.2
                
                # Special handling for key terms and acronyms
                if 'zmp' in query_lower or 'zero moment point' in query_lower:
                    if 'zmp' in section_title.lower() or 'zmp' in doc.lower():
                        base_similarity += 1.0
                
                if 'physical ai' in query_lower or 'physical artificial intelligence' in query_lower:
                    if 'physical ai' in section_title.lower() or 'physical ai' in doc.lower():
                        base_similarity += 1.0
                
                if 'humanoid' in query_lower and 'robot' in query_lower:
                    if 'humanoid' in section_title.lower() or 'humanoid' in chapter_title.lower():
                        base_similarity += 0.5
                
                # Boost for "what is" questions matching section titles
                if query_lower.startswith('what is') or query_lower.startswith('what are'):
                    # Extract the main topic from query
                    topic_words = query_lower.replace('what is ', '').replace('what are ', '').split()
                    for topic_word in topic_words:
                        if len(topic_word) > 3 and topic_word in section_title:
                            base_similarity += 0.3
                
                context_list.append({
                    "index": i + 1,
                    "content": doc,
                    "chapter_title": metadata.get("chapter_title", "Unknown"),
                    "section_title": metadata.get("section_title", "Unknown"),
                    "difficulty": metadata.get("difficulty", "Unknown"),
                    "similarity": base_similarity,
                    "metadata": metadata
                })
            
            # Sort by similarity (highest first)
            context_list.sort(key=lambda x: x["similarity"], reverse=True)
            
            # Return top 3
            return context_list[:3]
            
        except Exception as e:
            logger.error(f"Error retrieving context: {e}")
            return []
    
    async def generate_response(
        self,
        query: str,
        context: List[Dict[str, Any]],
        chat_history: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        Generate response based on query and retrieved context
        
        Args:
            query: User query
            context: Retrieved context documents
            chat_history: Optional chat history
            
        Returns:
            Dictionary with response and sources
        """
        # Build context text
        context_text = ""
        sources = []
        
        for i, ctx in enumerate(context, 1):
            context_text += f"\n\n[Source {i}]\n"
            context_text += f"Chapter: {ctx['chapter_title']}\n"
            context_text += f"Section: {ctx['section_title']}\n"
            context_text += f"Content: {ctx['content']}\n"
            
            sources.append({
                "chapter": ctx["chapter_title"],
                "section": ctx["section_title"],
                "similarity": round(ctx["similarity"] * 100, 1)
            })
        
        # Build prompt for LLM
        system_prompt = """You are an AI assistant for the Physical AI & Humanoid Robotics textbook. 
Your role is to help students understand concepts from the textbook.

Guidelines:
1. Base your answers primarily on the provided context from the textbook
2. If the context doesn't contain relevant information, acknowledge this limitation
3. Provide clear, educational explanations
4. Use examples when helpful
5. Cite which chapter/section your information comes from
6. Keep responses concise but informative
7. If asked about something outside the textbook scope, say so honestly"""

        user_prompt = f"""Context from textbook:
{context_text}

User Question: {query}

Please provide a helpful answer based on the textbook context above. Include citations to the sources you use."""

        # Use Qwen if available, otherwise use mock response
        if self.qwen_service.is_available():
            llm_result = await self.qwen_service.generate_response(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                chat_history=chat_history
            )
            response_text = llm_result.get("response", "")
        else:
            response_text = self._generate_mock_response(query, context)
        
        response = {
            "response": response_text,
            "sources": sources,
            "context_used": len(context) > 0,
            "confidence": max([c["similarity"] for c in context]) if context else 0,
            "qwen_available": self.qwen_service.is_available()
        }
        
        return response
    
    def _generate_mock_response(self, query: str, context: List[Dict[str, Any]]) -> str:
        """
        Generate a smart, professional, comprehensive response with enhanced formatting
        """
        if not context:
            return """I don't have specific information about that topic in the current textbook content.

**Suggested Topics I Can Help With:**
• **Humanoid Robots** - design, history, components, applications
• **Kinematics** - forward/inverse kinematics, DH parameters, DOF, Jacobian
• **Bipedal Walking** - ZMP (Zero Moment Point), CoM, balance control, gait generation
• **Physical AI** - embodiment, perception-action loop, sensorimotor contingencies
• **ROS 2** - nodes, topics, services, actions, rclpy, URDF
• **Gazebo Simulation** - physics engines, sensor simulation, plugins
• **NVIDIA Isaac** - Isaac Sim, Isaac Lab, synthetic data, RL training
• **VLA Models** - RT-2, GR00T, vision-language-action for robotics

Please try a question related to these topics from the Physical AI & Humanoid Robotics textbook."""

        best_match = context[0]
        chapter = best_match['chapter_title']
        section = best_match['section_title']
        content = best_match['content']

        # Clean content - extract just the main content part
        clean_content = content
        if "Chapter:" in clean_content and "Content:" in clean_content:
            content_idx = clean_content.find("Content:")
            clean_content = clean_content[content_idx + 8:].strip()

        # Smart response based on query type
        query_lower = query.lower()

        # Detect question type
        is_what = query_lower.startswith(('what ', 'what is', 'what are', 'define ', 'definition of'))
        is_how = query_lower.startswith(('how ', 'how does', 'how do'))
        is_explain = query_lower.startswith(('explain ', 'describe ', 'tell me about', 'teach me'))
        is_why = query_lower.startswith(('why ', 'why does', 'why do'))
        is_compare = query_lower.startswith(('compare ', 'difference between', 'vs '))

        # Extract paragraphs
        paragraphs = [p.strip() for p in clean_content.split('\n\n') if p.strip()]

        if not paragraphs:
            return "I found relevant information but couldn't extract a clear answer. Please try rephrasing your question or asking about a specific concept."

        response = []

        # Professional opening based on question type
        if is_what or is_explain:
            response.append(f"**{section}**")
            response.append("")
        elif is_how:
            response.append(f"**Understanding {section}**")
            response.append("")
        elif is_why:
            response.append(f"**Explanation: {section}**")
            response.append("")

        # Main answer - intelligent extraction and formatting
        main_answer = paragraphs[0]

        # For "what is" questions, provide complete definition with proper length
        if is_what or is_explain:
            if len(main_answer) > 300:
                # Find sentence boundary for natural truncation
                sentences = main_answer.split('. ')
                main_answer = '. '.join(sentences[:2])
                if len(main_answer) < 250 and len(sentences) > 2:
                    main_answer += '. ' + sentences[2]
                if len(main_answer) > 297:
                    main_answer = main_answer[:297] + "..."
        elif is_how or is_why:
            # For how/explain/why questions, combine first two paragraphs if available
            if len(paragraphs) > 1 and len(main_answer) < 200:
                main_answer = main_answer + " " + paragraphs[1]
            if len(main_answer) > 350:
                main_answer = main_answer[:347] + "..."
        else:
            # General questions
            if len(main_answer) > 300:
                main_answer = main_answer[:297] + "..."

        response.append(main_answer)
        response.append("")

        # Extract key points intelligently with better formatting
        key_points = []
        concepts_found = set()

        for para in paragraphs[1:]:
            para = para.strip()

            # Look for numbered lists, bullet points, or key concepts
            if para.startswith('-') or para.startswith('•') or (para[0].isdigit() and '. ' in para):
                point = para.lstrip('- ').lstrip('• ').strip()

                # Remove leading numbers
                if point and point[0].isdigit() and '. ' in point:
                    point = point.split('. ', 1)[1]

                # Extract concept and explanation
                if ':' in point:
                    parts = point.split(':', 1)
                    concept = parts[0].strip()
                    explanation = parts[1].strip()

                    # Avoid duplicates
                    if concept not in concepts_found:
                        concepts_found.add(concept)
                        # Clean up explanation length
                        if len(explanation) > 180:
                            explanation = explanation[:177] + "..."
                        key_points.append(f"• **{concept}**: {explanation}")
                else:
                    if point not in concepts_found:
                        concepts_found.add(point[:50])  # Use first 50 chars as key
                        key_points.append(f"• {point}")

                if len(key_points) >= 4:
                    break

            # Also look for important concepts in regular text
            elif len(key_points) < 3 and len(para) > 80:
                # Check if paragraph contains important concepts
                important_words = ['system', 'control', 'robot', 'motion', 'joint', 'sensor',
                                   'algorithm', 'model', 'framework', 'approach', 'method',
                                   'process', 'mechanism', 'technique', 'strategy']
                if any(word in para.lower() for word in important_words):
                    # Extract a key insight
                    if len(para) > 150:
                        para = para[:147] + "..."
                    key_points.append(f"• {para}")

        if key_points:
            response.append("**Key Insights:**")
            response.extend(key_points)
            response.append("")

        # Add related concepts from other context
        if len(context) > 1:
            related_sections = set()
            for ctx in context[1:]:
                related_sections.add(f"{ctx['section_title']}")

            if related_sections:
                response.append("**Related Concepts:**")
                for related in list(related_sections)[:3]:
                    response.append(f"→ {related}")
                response.append("")

        # Professional source attribution with difficulty level
        difficulty = best_match.get('difficulty', '')
        if difficulty:
            response.append(f"📖 *{chapter}* → **{section}** | Level: {difficulty}")
        else:
            response.append(f"📖 *{chapter}* → **{section}**")

        return "\n".join(response)
    
    async def chat(
        self,
        message: str,
        session_id: str = "default",
        chat_history: Optional[List[Dict[str, str]]] = None
    ) -> Dict[str, Any]:
        """
        Main chat interface
        
        Args:
            message: User message
            session_id: Session identifier
            chat_history: Optional chat history
            
        Returns:
            Response dictionary
        """
        # Retrieve relevant context
        context = self.retrieve_context(message)
        
        # Generate response
        response = await self.generate_response(message, context, chat_history)
        
        return {
            "response": response["response"],
            "sources": response["sources"],
            "session_id": session_id,
            "confidence": response["confidence"],
            "qwen_available": response.get("qwen_available", False)
        }


# Global RAG service instance
_rag_service = None

def get_rag_service() -> RAGService:
    """Get or create the global RAG service instance"""
    global _rag_service
    if _rag_service is None:
        _rag_service = RAGService()
    return _rag_service
