# Phase 5: Project Development Phase 💻

This directory contains the actual source code, templates, assets, and environmental configurations for the EduGenie application.

---

## 1. Project Directory Outline
- `app/`: Source code directory.
  - `app/main.py`: FastAPI server router, endpoints, schemas, and template renderers.
  - `app/ai_pipeline.py`: Groq/local model fallback service with prompt templates.
  - `app/config.py`: dot-env loader configurations.
  - `app/templates/index.html`: Responsive dashboard page.
  - `app/static/style.css`: Glassmorphic layout stylesheet.
- `.env`: (Ignored locally) Private settings containing your `GROQ_API_KEY`.
- `.env.example`: Configuration templates.

---

## 2. Local Execution Guide

### Step 1: Open the Development Directory
In your terminal, navigate into this folder:
```bash
cd "5. Project Development Phase"
```

### Step 2: Configure Environment
Copy `.env.example` to `.env` (if not done already) and insert your API key:
```env
GROQ_API_KEY=gsk_your_groq_key
```

### Step 3: Run the Application
Start the Uvicorn development server:
```bash
python -m uvicorn app.main:app --reload
```
Navigate to **http://127.0.0.1:8000** to use the application.
