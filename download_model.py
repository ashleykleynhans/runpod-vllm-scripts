#!/usr/bin/env python3
import os
from huggingface_hub import snapshot_download

if __name__ == "__main__":
    model_name = os.getenv("MODEL_NAME")

    if not model_name:
        raise ValueError("Must specify model name by adding MODEL_NAME environment variable")

    revision = os.getenv("MODEL_REVISION") or None
    snapshot_download(model_name, revision=revision, cache_dir=os.getenv("HF_HOME"))

    tokenizer_name = os.getenv("TOKENIZER_NAME") or None
    tokenizer_revision = os.getenv("TOKENIZER_REVISION") or None

    if tokenizer_name:
        snapshot_download(tokenizer_name, revision=tokenizer_revision, cache_dir=os.getenv("HF_HOME"))
