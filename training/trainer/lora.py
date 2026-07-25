"""
LoRA Configuration

Applies QLoRA adapters to the base model.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from unsloth import FastLanguageModel

from training.config import TrainingConfig


def apply_lora(model):

    print("=" * 60)
    print("Applying LoRA Configuration")
    print("=" * 60)

    model = FastLanguageModel.get_peft_model(

        model,

        # LoRA Parameters
        r=TrainingConfig.LORA_RANK,
        lora_alpha=TrainingConfig.LORA_ALPHA,
        lora_dropout=TrainingConfig.LORA_DROPOUT,

        # Train only attention & MLP layers
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],

        bias="none",

        use_gradient_checkpointing="unsloth",

        random_state=TrainingConfig.RANDOM_SEED,

    )

    print("✓ LoRA Applied Successfully")

    return model
