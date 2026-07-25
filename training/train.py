"""
QLoRA Training Script

Fine-tunes the Container Intelligence Advisor using Unsloth.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from datasets import load_dataset
from unsloth import FastLanguageModel

from config import TrainingConfig


def load_model():

    print("=" * 60)
    print("Loading Base Model")
    print("=" * 60)

    model, tokenizer = FastLanguageModel.from_pretrained(

        model_name=TrainingConfig.MODEL_NAME,

        max_seq_length=TrainingConfig.MAX_SEQ_LENGTH,

        dtype=None,

        load_in_4bit=True,

    )

    return model, tokenizer


def load_training_dataset():

    print("=" * 60)
    print("Loading Dataset")
    print("=" * 60)

    dataset = load_dataset(

        "json",

        data_files=TrainingConfig.DATASET_PATH,

        split="train",

    )

    print(f"Samples : {len(dataset)}")

    return dataset


def main():

    model, tokenizer = load_model()

    dataset = load_training_dataset()

    print()

    print("Model Loaded Successfully")

    print("Dataset Loaded Successfully")


if __name__ == "__main__":

    main()
