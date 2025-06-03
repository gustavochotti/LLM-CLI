# tests/test_generator.py
# python -m pytest -s tests/
import pytest
from generator import generate_text, load_pipeline


def test_generate_text_valid():
    prompt = "Explain what is artificial intelligence"
    result = generate_text(prompt, "google/flan-t5-base", 50)
    assert isinstance(result, str)
    assert len(result.strip()) > 0


def test_generate_text_empty_prompt():
    with pytest.raises(ValueError):
        generate_text("", "google/flan-t5-base", 50)


def test_load_pipeline_valid():
    model = load_pipeline("google/flan-t5-base")
    assert callable(model)


def test_load_pipeline_invalid():
    with pytest.raises(Exception):
        load_pipeline("invalid-model-name-that-does-not-exist")
