# Phase 7: Project Documentation 📚

This phase documents REST API specifications, system architecture designs, and hotfixes resolved during setup.

---

## 1. REST API Specification

### Endpoint: `POST /api/qa`
- **Request Body**: `{"question": "string"}` (Length: 3 to 5000 chars)
- **Response**: `{"result": "string", "model_used": "string"}`

### Endpoint: `POST /api/explain`
- **Request Body**: `{"concept": "string"}` (Length: 2 to 1000 chars)
- **Response**: `{"result": "string", "model_used": "string"}`

### Endpoint: `POST /api/quiz`
- **Request Body**: `{"topic": "string"}` (Length: 2 to 1000 chars)
- **Response**: `{"result": "string", "model_used": "string"}`

### Endpoint: `POST /api/summarize`
- **Request Body**: `{"text": "string"}` (Length: 10 to 15000 chars)
- **Response**: `{"result": "string", "model_used": "string"}`

### Endpoint: `POST /api/learning-path`
- **Request Body**: `{"topic": "string"}` (Length: 2 to 1000 chars)
- **Response**: `{"result": "string", "model_used": "string"}`

---

## 2. Dynamic Fallback Logic
The system attempts to call the Groq client. If the `GROQ_API_KEY` is not present, or if the API call raises an exception (network failure, quota limit, timeout), it immediately runs:
```python
generate_with_local(prompt_local)
```
This loads PyTorch and the `transformers` pipeline to run `LaMini-Flan-T5-77M` locally. To optimize local performance, we added:
- `repetition_penalty=1.3` (avoids word/phrase repetition loops).
- `no_repeat_ngram_size=3` (prevents copy-paste options).

---

## 3. Environment Resolution Logs
- **Issue 1**: Duplicate package metadata directory conflicts for `packaging` package on Anaconda (`found=None`), causing `transformers` loading failure.
  - *Fix*: Deleted duplicate `.dist-info` directories and ran clean `pip install packaging==26.2`.
- **Issue 2**: Keras 3 dependency checking errors within `transformers` on Python 3.13.
  - *Fix*: Injected `os.environ["USE_TF"] = "NO"` at the top level of entrypoint scripts to skip TensorFlow checks entirely.
