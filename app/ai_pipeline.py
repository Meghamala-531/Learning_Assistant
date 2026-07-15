import os
os.environ["USE_TF"] = "NO"

import logging
from typing import Tuple
import torch
from groq import Groq
from transformers import pipeline

from app.config import GROQ_API_KEY, LOCAL_MODEL_NAME

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Groq client
groq_client = None
if GROQ_API_KEY:
    try:
        groq_client = Groq(api_key=GROQ_API_KEY)
        logger.info("Groq client initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize Groq client: {e}")
else:
    logger.warning("GROQ_API_KEY not found or empty. EduGenie will use the local model by default.")

# Lazy loader for local transformers model
_local_pipeline = None

def get_local_pipeline():
    global _local_pipeline
    if _local_pipeline is None:
        logger.info(f"Loading local model '{LOCAL_MODEL_NAME}'...")
        
        # Select device: GPU if available, else MPS (macOS Apple Silicon), else CPU
        if torch.cuda.is_available():
            device = 0
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            device = "mps"
        else:
            device = -1
            
        logger.info(f"Using device: {'cuda' if device == 0 else ('mps' if device == 'mps' else 'cpu')}")
        
        try:
            # Load text2text-generation pipeline
            _local_pipeline = pipeline(
                "text2text-generation",
                model=LOCAL_MODEL_NAME,
                device=device
            )
            logger.info("Local model loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading local model: {e}")
            raise e
    return _local_pipeline

def generate_with_groq(prompt: str, model: str = "llama-3.3-70b-versatile") -> str:
    """Helper to generate text using Groq API."""
    if not groq_client:
        raise ValueError("Groq client is not initialized (missing API key).")
    
    completion = groq_client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are EduGenie, a helpful and knowledgeable AI educational assistant."},
            {"role": "user", "content": prompt}
        ],
        model=model,
        temperature=0.7,
        max_tokens=1024,
    )
    return completion.choices[0].message.content.strip()

def generate_with_local(prompt: str) -> str:
    """Helper to generate text using the local fallback model."""
    nlp = get_local_pipeline()
    outputs = nlp(
        prompt, 
        max_length=512, 
        do_sample=True,
        temperature=0.7,
    )
    return outputs[0]['generated_text'].strip()

def generate_response(prompt_groq: str, prompt_local: str) -> Tuple[str, str]:
    """
    Attempts to generate a response using Groq. 
    Falls back to the local model if Groq fails or is not configured.
    Returns: Tuple of (response_text, model_used)
    """
    if groq_client:
        try:
            logger.info("Attempting generation using Groq API...")
            response = generate_with_groq(prompt_groq)
            return response, "Groq (llama-3.3-70b-versatile)"
        except Exception as e:
            logger.error(f"Groq API call failed: {e}. Falling back to local model.")
            # Fall through to local model
            
    try:
        logger.info("Generating response using local model...")
        response = generate_with_local(prompt_local)
        return response, f"Local Fallback ({LOCAL_MODEL_NAME})"
    except Exception as e:
        logger.error(f"Local model generation failed: {e}")
        return f"Error: Failed to generate response from both Groq and local fallback. Details: {e}", "None"

def get_question_answering(question: str) -> Tuple[str, str]:
    """Provide an accurate direct answer plus brief educational context."""
    prompt_groq = f"Provide a direct, accurate answer to this educational question, followed by brief educational context or explanations. Keep the tone helpful, clear, and educational.\n\nQuestion: {question}"
    prompt_local = f"Answer this question clearly and provide brief educational context: {question}"
    return generate_response(prompt_groq, prompt_local)

def get_concept_explanation(concept: str) -> Tuple[str, str]:
    """Explain a concept in simple terms, using analogies if helpful."""
    prompt_groq = f"Explain the concept '{concept}' in simple, easy-to-understand terms. Use analogies, real-world examples, or breakdowns suitable for a student. Keep it engaging."
    prompt_local = f"Explain this concept simply with a real-world example: {concept}"
    return generate_response(prompt_groq, prompt_local)

def get_quiz_generation(topic: str) -> Tuple[str, str]:
    """Generate a topic-specific quiz."""
    prompt_groq = (
        f"Create an educational quiz on the topic: '{topic}'.\n"
        f"Format it as a 5-question multiple choice quiz. For each question, list options A, B, C, and D. "
        f"At the very end of the quiz, provide a clear 'Answer Key' indicating the correct option for each question (e.g. 1. A, 2. B, etc.). "
        f"Do not show the correct answer inline with the question."
    )
    prompt_local = f"Generate 3 simple multiple-choice questions and answers for a quiz about {topic}."
    return generate_response(prompt_groq, prompt_local)

def get_text_summarization(text: str) -> Tuple[str, str]:
    """Summarize educational text."""
    prompt_groq = f"Summarize the following educational text. Highlight the core concepts, main ideas, and key takeaways in a clear, bulleted format.\n\nText:\n{text}"
    prompt_local = f"Summarize this text, focusing on the main educational points: {text}"
    return generate_response(prompt_groq, prompt_local)

def get_learning_path(topic: str) -> Tuple[str, str]:
    """Generate a personalized learning path with study guidance."""
    prompt_groq = (
        f"Create a structured, step-by-step educational learning path / roadmap for the topic: '{topic}'.\n"
        f"Divide it into three logical stages: Beginner, Intermediate, and Advanced.\n"
        f"For each stage, specify:\n"
        f"- Core topics to study\n"
        f"- Suggested study guidance / exercises\n"
        f"- Suggested projects or check-points\n"
        f"Keep the structure clean and readable."
    )
    prompt_local = f"Create a beginner, intermediate, and advanced learning roadmap for: {topic}"
    return generate_response(prompt_groq, prompt_local)

