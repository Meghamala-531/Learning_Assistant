import os
os.environ["USE_TF"] = "NO"

import logging
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app.ai_pipeline import (
    get_question_answering,
    get_concept_explanation,
    get_quiz_generation,
    get_text_summarization,
    get_learning_path,
)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="EduGenie - AI Educational Assistant",
    description="An AI educational assistant powering learning through questions, summaries, quizzes, roadmaps, and explanations.",
    version="1.0.0",
)

# Set up paths
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# Create directories if they do not exist (to prevent FastAPI mount failures)
STATIC_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)

# Mount static files and templates
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

# Pydantic Schemas for Requests
class QARequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=5000, description="The educational question to answer")

class ExplainRequest(BaseModel):
    concept: str = Field(..., min_length=2, max_length=1000, description="The concept to explain")

class QuizRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=1000, description="The topic to generate a quiz for")

class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=15000, description="The educational text to summarize")

class LearningPathRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=1000, description="The topic to generate a learning path for")


# Web Route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Renders the main dashboard page."""
    return templates.TemplateResponse(request, "index.html")


# API Routes
@app.post("/api/qa")
async def api_qa(req: QARequest):
    """API Endpoint for Question Answering."""
    try:
        ans, model = get_question_answering(req.question)
        return JSONResponse(content={"result": ans, "model_used": model})
    except Exception as e:
        logger.error(f"Error in /api/qa: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while answering your question: {str(e)}"
        )

@app.post("/api/explain")
async def api_explain(req: ExplainRequest):
    """API Endpoint for Concept Explanation."""
    try:
        exp, model = get_concept_explanation(req.concept)
        return JSONResponse(content={"result": exp, "model_used": model})
    except Exception as e:
        logger.error(f"Error in /api/explain: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while explaining the concept: {str(e)}"
        )

@app.post("/api/quiz")
async def api_quiz(req: QuizRequest):
    """API Endpoint for Quiz Generation."""
    try:
        quiz, model = get_quiz_generation(req.topic)
        return JSONResponse(content={"result": quiz, "model_used": model})
    except Exception as e:
        logger.error(f"Error in /api/quiz: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while generating the quiz: {str(e)}"
        )

@app.post("/api/summarize")
async def api_summarize(req: SummarizeRequest):
    """API Endpoint for Text Summarization."""
    try:
        summary, model = get_text_summarization(req.text)
        return JSONResponse(content={"result": summary, "model_used": model})
    except Exception as e:
        logger.error(f"Error in /api/summarize: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while summarizing the text: {str(e)}"
        )

@app.post("/api/learning-path")
async def api_learning_path(req: LearningPathRequest):
    """API Endpoint for Learning Path Recommendation."""
    try:
        path, model = get_learning_path(req.topic)
        return JSONResponse(content={"result": path, "model_used": model})
    except Exception as e:
        logger.error(f"Error in /api/learning-path: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while generating the learning path: {str(e)}"
        )
