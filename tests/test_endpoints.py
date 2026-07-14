from unittest.mock import patch
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_root():
    """Verify that root URL serves the HTML index page."""
    response = client.get("/")
    assert response.status_code == 200
    assert "EduGenie" in response.text
    assert "Question Answering" in response.text

@patch("app.main.get_question_answering")
def test_api_qa(mock_qa):
    """Verify the question answering endpoint."""
    mock_qa.return_value = ("The largest ocean is the Pacific Ocean.", "Groq (Mock)")
    response = client.post("/api/qa", json={"question": "Which is the largest ocean?"})
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert "model_used" in data
    assert data["result"] == "The largest ocean is the Pacific Ocean."
    assert data["model_used"] == "Groq (Mock)"
    mock_qa.assert_called_once_with("Which is the largest ocean?")

@patch("app.main.get_concept_explanation")
def test_api_explain(mock_exp):
    """Verify the concept explanation endpoint."""
    mock_exp.return_value = ("Photosynthesis is how plants make food.", "Local Fallback (Mock)")
    response = client.post("/api/explain", json={"concept": "Photosynthesis"})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == "Photosynthesis is how plants make food."
    assert data["model_used"] == "Local Fallback (Mock)"
    mock_exp.assert_called_once_with("Photosynthesis")

@patch("app.main.get_quiz_generation")
def test_api_quiz(mock_quiz):
    """Verify the quiz generation endpoint."""
    mock_quiz.return_value = ("1. What is 2+2?\nA) 3\nB) 4\nAnswer Key:\n1. B", "Groq (Mock)")
    response = client.post("/api/quiz", json={"topic": "Math"})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == "1. What is 2+2?\nA) 3\nB) 4\nAnswer Key:\n1. B"
    assert data["model_used"] == "Groq (Mock)"
    mock_quiz.assert_called_once_with("Math")

@patch("app.main.get_text_summarization")
def test_api_summarize(mock_sum):
    """Verify the summarization endpoint."""
    mock_sum.return_value = ("This is a test summary.", "Groq (Mock)")
    response = client.post(
        "/api/summarize", 
        json={"text": "This is a very long text to summarize, and it needs to meet length requirements."}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == "This is a test summary."
    assert data["model_used"] == "Groq (Mock)"
    mock_sum.assert_called_once()

@patch("app.main.get_learning_path")
def test_api_learning_path(mock_lp):
    """Verify the learning path recommendation endpoint."""
    mock_lp.return_value = ("Step 1: Learn SQL. Step 2: Practice.", "Groq (Mock)")
    response = client.post("/api/learning-path", json={"topic": "SQL"})
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == "Step 1: Learn SQL. Step 2: Practice."
    assert data["model_used"] == "Groq (Mock)"
    mock_lp.assert_called_once_with("SQL")

def test_api_validation_error():
    """Verify input validation triggers a 422 Unprocessable Entity error."""
    # Question too short (under 3 chars)
    response = client.post("/api/qa", json={"question": "ab"})
    assert response.status_code == 422
