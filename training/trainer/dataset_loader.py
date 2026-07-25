"""
Dataset Loader

Loads the training dataset.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from datasets import load_dataset

from training.config import TrainingConfig


def load_training_dataset():

    print("=" * 60)
    print("Loading Training Dataset")
    print("=" * 60)

    print(f"Dataset : {TrainingConfig.DATASET_PATH}")

    dataset = load_dataset(

        "json",

        data_files=TrainingConfig.DATASET_PATH,

        split="train",

    )

    print(f"✓ Loaded {len(dataset)} samples")

    return dataset
