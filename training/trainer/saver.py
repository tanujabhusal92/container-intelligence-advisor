"""
Model Saver

Saves the trained LoRA adapter and tokenizer.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""


from training.config import TrainingConfig


def save_model(
    model,
    tokenizer,
):

    print("=" * 60)
    print("Saving Model Adapter")
    print("=" * 60)


    model.save_pretrained(

        TrainingConfig.OUTPUT_DIR

    )


    tokenizer.save_pretrained(

        TrainingConfig.OUTPUT_DIR

    )


    print(
        f"✓ Model saved at {TrainingConfig.OUTPUT_DIR}"
    )
