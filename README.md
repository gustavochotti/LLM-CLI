# 💬 LLM CLI - Text Generation

This is a Python CLI project for generating text using Hugging Face Transformers models.

---

## ✅ Features
- Text generation using `text2text-generation`
- Professional logging via Python's `logging` module
- Unit tests with `pytest`
- CLI interface via `argparse`

---

## 🚀 How to Use

```bash
python -m main --prompt "What is artificial intelligence?"
```

### Options:
- `--model`: Hugging Face model name (default: `google/flan-t5-large`)
- `--tokens`: Maximum number of tokens to generate (default: 512)

---

## 🧪 Running Tests

```bash
pip install pytest
python -m pytest -s tests/
```

---

## ⚠️ Default Model Limitations
The default model is `google/flan-t5-large`, which has:

- 🔹 Short, instruction-following responses
- 🔹 Limited capabilities for long-form or creative generation
- 🔹 Best suited for QA, translation, classification

> For creative and extended generation, consider switching to `mistralai/Mistral-7B-Instruct-v0.1`

---

## 📦 Requirements
- Python 3.8+
- `transformers`
- `pytest` (for testing only)

---

## 📁 Project Structure
```
llm/
├── config.py
├── errors.py
├── generator.py
├── main.py
├── __init__.py

tests/
├── test_generator.py
```

---

## 🛠️ Roadmap
- API support (OpenAI / Gemini)
- Multi-task support (summarization, QA, etc.)
- Web UI frontend
