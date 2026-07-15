<<<<<<< HEAD
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
=======
# 🧞‍♂️ EduGenie — Your AI Learning Genie! ✨

EduGenie is a super lightweight, responsive AI educational assistant. It helps students, self-learners, and educators by answering questions, simplifying concepts, generating quizzes, summarizing textbooks, and creating roadmaps.

This repository is structured into **8 Software Development Life Cycle (SDLC) phases** matching clean project documentation standards.

---

## 📂 Repository Structure

* [**`1. Brainstorming & Ideation/`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/1.%20Brainstorming%20&%20Ideation): Product conceptualization, target audience, and features ideation.
* [**`2. Requirement Analysis/`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/2.%20Requirement%20Analysis): System requirements, functional/non-functional analyses.
* [**`3. Project Design Phase/`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/3.%20Project%20Design%20Phase): High-level system architecture, flowcharts, and diagrams.
* [**`4. Project Planning Phase/`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/4.%20Project%20Planning%20Phase): Sprints schedule, milestone tracking, and task lists.
* [**`5. Project Development Phase/`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/5.%20Project%20Development%20Phase): **Source code folder** (`app/`), environmental variables, and configs.
* [**`6. Project Testing/`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/6.%20Project%20Testing): Integration test suites and pytest scripts.
* [**`7. Project Documentation/`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/7.%20Project%20Documentation): REST API specifications, fallback design, and environmental fixes.
* [**`8. Project Demonstration/`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/8.%20Project%20Demonstration): Application walkthroughs and interface demonstrations.

---

## 🛠️ Quick Setup & Run

### 1. Install Dependencies
Run from the root directory:
```bash
pip install -r requirements.txt
```

### 2. Configure Keys 🔑
Open [**`5. Project Development Phase/.env`**](file:///c:/Users/ganes/Desktop/Learning%20_Assistant/5.%20Project%20Development%20Phase/.env) and insert your Groq API key:
```env
GROQ_API_KEY=gsk_your_groq_key
```
*(If left blank, it automatically downloads and runs the `LaMini-Flan-T5` model locally offline!)*

### 3. Start the Server! 🚀
Navigate into the development folder and run the server:
```bash
cd "5. Project Development Phase"
python -m uvicorn app.main:app --reload
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser!

---

## 🧪 Running Tests
To run the integration tests, execute from the root directory:
```bash
python -m pytest "6. Project Testing/tests"
```

---

## 👤 Author / Team Members

* **Thaamarapalli Meghamala** (Project Leader)
  - **Email**: [tmeghamala531@gmail.com](mailto:tmeghamala531@gmail.com)
  - **GitHub**: [Meghamala-531](https://github.com/Meghamala-531)

* **Rama Krishna Vedantam**
  - **Email**: [krishna.vssr@gmail.com](mailto:krishna.vssr@gmail.com)

* **Sarala Avurthula**
  - **Email**: [saralajaggarao03@gmail.com](mailto:saralajaggarao03@gmail.com)

* **Prasanna Thadepalli**
  - **Email**: [tadepalliprasanna81@gmail.com](mailto:tadepalliprasanna81@gmail.com)

* **Jetti Tarun Kumar**
  - **Email**: [jettitarunkumaryadav67@gmail.com](mailto:jettitarunkumaryadav67@gmail.com)
>>>>>>> 80ff54e57c9220d64992ca3d94f55c9d3a29a297
