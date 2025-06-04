# config.py

# Default model for text generation
MODEL_NAME = "google/flan-t5-large"

# Default maximum number of new tokens to generate
MAX_NEW_TOKENS = 512

# Device to run the model on. Options: "cpu", "cuda" (if CUDA-enabled GPU is available).
# The transformers library typically handles device placement well if 'cuda' is chosen and available.
# For pipeline, device=0 means first CUDA device, device=-1 means CPU.
DEVICE = "cpu"
