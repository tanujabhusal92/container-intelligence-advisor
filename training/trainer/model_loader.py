"""
Model Loader

Loads the base LLM and tokenizer.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from unsloth import FastLanguageModel

from training.config import TrainingConfig


def load_model():

    print("=" * 60)
    print("Loading Base Model")
    print("=" * 60)

    print(f"Model : {TrainingConfig.MODEL_NAME}")

    model, tokenizer = FastLanguageModel.from_pretrained(

        model_name=TrainingConfig.MODEL_NAME,

        max_seq_length=TrainingConfig.MAX_SEQ_LENGTH,

        dtype=None,

        load_in_4bit=True,

    )

    print("✓ Model Loaded Successfully")

    return model, tokenizer
