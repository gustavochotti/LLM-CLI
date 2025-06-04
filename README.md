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
- `--model MODEL_NAME`: Hugging Face model name
   * Default `google/flan-t5-large`. This tool is primarily designed for text2text-generation models.
   * To change the script's default model, modify the `MODEL_NAME` variable in the `config.py` file.
- `--tokens MAX_TOKENS`:Maximum number of new tokens to generate
  * Default: `512`
  * To change the script's default token limit, modify the `MAX_NEW_TOKENS` variable in `config.py`

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

> For creative and extended generation, consider switching to models like `mistralai/Mistral-7B-Instruct-v0.1`

If you choose to use a model like `mistralai/Mistral-7B-Instruct-v0.1` (a powerful instruction-following `text-generation` model) or similar large language models (LLMs), please note the following:

* **Task Type:**
    * Models like `mistralai/Mistral-7B-Instruct-v0.1` is primarily a `text-generation` (auto-regressive or causal) model, not a `text2text-generation` (encoder-decoder) model like T5 or BART.
    * The CLI is currently configured to use `task="text2text-generation"` when loading the pipeline in the `generator.py` file. For optimal results with powerful models, **you will likely need to change this parameter to `task="text-generation"`** in the `load_pipeline_from_cache` function in `generator.py`.
    * Without this change, the model might not behave as expected (e.g., it might try to continuously complete your prompt rather than follow an instruction and stop).

* **Resource Requirements:**
    * Powerful models will require significantly more RAM (for CPU mode) or VRAM (for GPU mode) compared to the default `google/flan-t5-large`.
    * The model download size will be substantial (several gigabytes).
    * Text generation (inference) will be slower, especially on CPU.

**To experiment with models like this using the CLI (with potential code modifications):**

1.  Ensure you have sufficient system resources (RAM/VRAM, disk space).
2.  Use the `--model` argument:
   
    ```bash
    python -m main --prompt "Write a short sci-fi story about an AI that discovers emotion." --model "mistralai/Mistral-7B-Instruct-v0.1" --tokens 300
    ```
    
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
python -m main --prompt "Write a short poem about the moon." --model "google/flan-t5-small" --tokens 256
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
