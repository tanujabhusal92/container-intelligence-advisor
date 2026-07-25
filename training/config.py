"""
Training Configuration

Central configuration for QLoRA training.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""


from pathlib import Path



class TrainingConfig:


    # -------------------------------------------------
    # Model Configuration
    # -------------------------------------------------

    MODEL_NAME = (
        "unsloth/Llama-3.2-3B-Instruct"
    )


    MAX_SEQ_LENGTH = 2048



    # -------------------------------------------------
    # Dataset
    # -------------------------------------------------

    DATASET_PATH = (
        "dataset/output/train.jsonl"
    )



    # -------------------------------------------------
    # LoRA Configuration
    # -------------------------------------------------

    LORA_RANK = 16

    LORA_ALPHA = 16

    LORA_DROPOUT = 0.0



    # -------------------------------------------------
    # Training Parameters
    # -------------------------------------------------

    OUTPUT_DIR = (
        "models/container-intelligence-advisor-lora"
    )


    BATCH_SIZE = 2


    GRADIENT_ACCUMULATION = 4


    LEARNING_RATE = 2e-4


    NUM_EPOCHS = 3


    WARMUP_STEPS = 10


    LOGGING_STEPS = 10



    # -------------------------------------------------
    # Reproducibility
    # -------------------------------------------------

    RANDOM_SEED = 42
