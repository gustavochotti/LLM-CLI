# 💬 LLM CLI - Text Generation

This is a Python CLI project for generating text using Hugging Face Transformers models.

---

## ✅ Features
- Text generation using `text2text-generation`
- Logging via Python's `logging` module
- Unit tests with `pytest`
- CLI interface via `argparse`

---

## ⚙️ Options:
- `--prompt TEXT`: (Required) The input text to generate a response from.
- `--model MODEL_NAME`: Hugging Face model name (default: `google/flan-t5-large`). This tool is primarily designed for text2text-generation models.
- `--tokens MAX_TOKENS`:Maximum number of new tokens to generate (default: 512).

---

## 🧠 Model Management:
This CLI utilizes models from the Hugging Face Hub via the `transformers` library.

- Automatic Download & Caching: Models specified via the `--model` option (or the default model) are automatically downloaded the first time they are used. They are then stored in a local cache (typically `~/.cache/huggingface/transformers/` or `~/.cache/huggingface/hub/`) for faster access in subsequent uses. Ensure you have an internet connection when using a new model for the first time.
- Model Compatibility: This tool is primarily designed for `text2text-generation` models (e.g., T5, BART). For a list of available models, you can explore the [Hugging Face Model Hub for text2text-generation](https://huggingface.co/models?pipeline_tag=text2text-generation)
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
├── tests/
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

Using a different model and specifying token count:
```bash
python main.py --prompt "Write a short poem about the moon." --model "t5-small" --tokens 100
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

## 🛠️ Roadmap
- Multi-task support (summarization, QA, etc.)
- Allow passing generation parameters (temperature, top_p, etc.) via CLI.
- More robust model compatibility checking.
- Web UI frontend

---

# 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
