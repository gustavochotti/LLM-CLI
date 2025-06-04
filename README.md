# 💬 LLM CLI - Text Generation

This is a Python CLI project for generating text using Hugging Face Transformers models.

---

## ✅ Features
- Text generation using `text2text-generation`
- Logging via Python's `logging` module
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

## 📁 Project Structure
```
LLM-CLI/
├── config.py
├── logger.py
├── errors.py
├── generator.py
├── main.py
├── __init__.py

tests/
├── test_generator.py
```

---

## 📦 Requirements
- Python 3.8+
- `transformers`
- `Pip` (Python package installer)
- `pytest` (for testing only)

---

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/gustavochotti/LLM-CLI.git](https://github.com/gustavochotti/LLM-CLI.git)
    cd LLM-CLI
    ```

2.  **(Recommended)** Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 How to Use

Once installed, you can generate text by running the `main.py` script from the project's root directory:

```bash
python -m main --prompt "What is artificial intelligence?"
```

---

## 💡 Example Output

```bash
$ python -m main --prompt "What is artificial intelligence?"
[INFO] Device set to use cpu
[INFO] google/flan-t5-large | RESPONSE:
Artificial intelligence is the simulation of human intelligence by machines that are programmed to think and learn.
```

---

---

## 🛠️ Roadmap
- Multi-task support (summarization, QA, etc.)
- Web UI frontend
