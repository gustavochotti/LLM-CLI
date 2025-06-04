# main.py
import argparse
from generator import generate_text
from config import MODEL_NAME, MAX_NEW_TOKENS, DEVICE
from logger import log_info, log_error

def main():
    parser = argparse.ArgumentParser(description="Generate text using Hugging Face Transformers.")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt text for generation")
    parser.add_argument("--model", type=str, default=MODEL_NAME, help="Model name (default: google/flan-t5-large)")
    parser.add_argument("--tokens", type=int, default=MAX_NEW_TOKENS, help="Max new tokens to generate")

    args = parser.parse_args()

    try:
        log_info(f"Device set to use {DEVICE}")
        output = generate_text(args.prompt, args.model, args.tokens)
        log_info(f"{args.model} | RESPONSE:\n{output}")
    except ValueError as ve:
        log_error(f"{ve}")
    except Exception as e:
        log_error(f"Unexpected failure: {e}")

if __name__ == "__main__":
    main()
