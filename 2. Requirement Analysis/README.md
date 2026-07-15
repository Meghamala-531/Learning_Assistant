# Phase 2: Requirement Analysis 📋

This phase outlines what the EduGenie software system must accomplish to satisfy user needs.

---

## 1. Functional Requirements

### FR1: User Dashboard Interface
- Single-page application using responsive tabs.
- Dedicated input/action triggers for each of the 5 core features.
- High-contrast visual loading indicator during AI generation requests.

### FR2: Primary AI Service Engine
- Integration with Groq API running state-of-the-art LLMs (e.g. `llama-3.3-70b-versatile`).
- Seamless connection and fast inference times.

### FR3: Local Fallback Engine
- Local offline execution utilizing Hugging Face `transformers` and `PyTorch` with the `MBZUAI/LaMini-Flan-T5-77M` model.
- Automatically takes over if the Groq API key is missing or fails (network errors, rate-limits).

### FR4: Markdown Formatting & Output Processing
- Direct on-the-fly markdown parsing for AI outputs.
- Separation of Quiz questions and the Answer Key using client-side parsers.

---

## 2. Non-Functional Requirements

### NFR1: Performance & Startup
- Zero application startup delay.
- The heavy local model must load *lazily* (only upon the first failed/empty Groq call) to ensure instant startup.

### NFR2: Portability & Hardware Constraints
- Minimal resource profile suitable to run on lightweight hardware (including M1 class macOS machines or local windows setups).

### NFR3: Security
- Secure environment configuration. Secret API keys must never be committed or pushed to public repositories.
