# Phase 4: Project Planning Phase 📅

This phase documents the scheduling, checks, and sprints tracked during the implementation of the EduGenie project.

---

## 1. Development Roadmap (Checkpoints)

* **Checkpoint 1: Workspace setup**
  - Dependency definitions (`requirements.txt`) and setup configurations.
* **Checkpoint 2: Model integrations**
  - Groq SDK connection tests and local Hugging Face `transformers` loader.
* **Checkpoint 3: Backend API routes**
  - FastAPI server setup, mounting assets, and Pydantic validation structures.
* **Checkpoint 4: Frontend styling & layouts**
  - Tab routing script, glassmorphic layout stylesheet, and error catch banners.
* **Checkpoint 5: System testing & verification**
  - Unit tests verifying mock generation routes and debugging import errors.

---

## 2. Sprint Timeline Tracker
- **Sprint 1 (Environment Setup)**: Configure virtual environment, set up gitignore rules to secure keys, configure configs.
- **Sprint 2 (Backend AI & APIs)**: Build `ai_pipeline.py` fallback logics, create the FastAPI server and endpoints.
- **Sprint 3 (Frontend & Output Processing)**: Create the UI panel, integrate marked.js and quiz answer splitters.
- **Sprint 4 (Testing & Deployment)**: Execute pytest cases, hotfix package metadata mismatches, and deploy locally.
