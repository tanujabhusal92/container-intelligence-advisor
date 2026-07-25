"""
Training Configuration

Central configuration for QLoRA training.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from dataclasses import dataclass


@dataclass
class TrainingConfig:

    # -----------------------------
    # Base Model
    # -----------------------------

    MODEL_NAME = "unsloth/Llama-3.2-3B-Instruct"

    # -----------------------------
    # Dataset
    # -----------------------------

    DATASET_PATH = "../dataset/output/train.jsonl"

    # -----------------------------
    # Output
    # -----------------------------

    OUTPUT_DIR = "../models/container-intelligence-advisor"

    # -----------------------------
    # LoRA
    # -----------------------------

    LORA_RANK = 16

    LORA_ALPHA = 16

    LORA_DROPOUT = 0

    # -----------------------------
    # Training
    # -----------------------------

    MAX_SEQ_LENGTH = 2048

    BATCH_SIZE = 2

    GRADIENT_ACCUMULATION = 4

    LEARNING_RATE = 2e-4

    NUM_EPOCHS = 3

    WARMUP_STEPS = 10

    LOGGING_STEPS = 10

    SAVE_STEPS = 100

    RANDOM_SEED = 42
