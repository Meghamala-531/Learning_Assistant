# Phase 6: Project Testing 🧪

This directory contains the integration and validation test suite for checking backend logic, endpoint handlers, request constraints, and fallback mechanisms.

---

## 1. Automated Integration Tests
The testing directory contains `tests/test_endpoints.py` which validates:
- `test_read_root`: Serves the HTML frontend dashboard.
- `test_api_qa`: Validates correct inputs and outputs for Question Answering.
- `test_api_explain`: Validates Concept Explanation formats.
- `test_api_quiz`: Verifies MCQ quiz structures and output returns.
- `test_api_summarize`: Assures length validation constraints and text compression.
- `test_api_learning_path`: Verifies step-by-step roadmap structures.
- `test_api_validation_error`: Ensures short/empty inputs trigger a `422 Unprocessable Entity` response.

*Note: Test files patch/mock the generation layer (`generate_response`) so tests run instantly, offline, and require no API key.*

---

## 2. How to Run the Tests
Execute the following command in your terminal from the root folder:
```bash
python -m pytest "6. Project Testing/tests"
```
You will see output indicating that all 7 tests have passed.
