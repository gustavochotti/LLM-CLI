# llm/generator.py
from transformers import pipeline
from config import DEVICE
from errors import handle_exception
from logger import log_error

def load_pipeline(model_name: str):
    task = "text2text-generation"
    try:
        return pipeline(task, model=model_name, device=0 if DEVICE == "cuda" else -1)
    except Exception as e:
        handle_exception(e, f"Failed to load model '{model_name}'")
        raise

def generate_text(prompt: str, model_name: str, max_tokens: int) -> str:
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("Prompt is empty or invalid.")

    prompt = f"Instruction: {prompt.strip()}"

    try:
        generator = load_pipeline(model_name)
        output = generator(
            prompt,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.9,
            repetition_penalty=1.2,
            no_repeat_ngram_size=3
        )
        return output[0].get("generated_text") or output[0].get("text", "[No output]")
    except Exception as e:
        handle_exception(e, "Text generation failed")
        return "[ERROR] Text generation failed."