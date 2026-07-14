# Phase 3: Project Design Phase 🎨

This phase explains the system architecture, flow patterns, and file structure design of the EduGenie application.

---

## 1. System Flow Architecture

```mermaid
graph TD
    Client[Web Browser Frontend] -->|1. Submit HTTP Request| Server[FastAPI Backend Server]
    Server -->|2. Route Request| Route[API Endpoint Handlers]
    Route -->|3. Call Generation| Pipeline[AI Service Pipeline]
    
    subgraph AI Service Layer
        Pipeline -->|4. Check Key| Decision{Groq API Key Configured?}
        Decision -->|Yes| Groq[Groq LPU Llama 3.3 Engine]
        Decision -->|No / Exception| Fallback[Local LaMini-Flan-T5 Model]
        Groq -->|Success| Out[Return Output + Metadata]
        Fallback -->|Lazy Load weights| Out
    end
    
    Out -->|5. Return JSON Response| Route
    Route -->|6. Send Response| Client
    Client -->|7. Render Markdown & Format Quizzes| Display[User Dashboard]
```

---

## 2. Component Design Breakdown

- **Web Frontend Component**: Standard HTML5, CSS Grid/Flexbox layout, and JavaScript. Uses `marked.js` library for client-side markdown compiling.
- **FastAPI Routing Layer**: Pydantic request models ensure input length constraints and data types are verified. 
- **Configuration Module**: Uses `python-dotenv` to securely inject configurations from a local `.env` file into application runtime environment variables.
- **AI Pipeline Module**: Manages dual-generation logic. Isolates PyTorch execution environments and applies repetition penalties and length constraints.
