"""
Trainer Builder

Creates the supervised fine-tuning trainer.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from trl import SFTTrainer
from transformers import TrainingArguments

from training.config import TrainingConfig


def create_trainer(
    model,
    tokenizer,
    dataset,
):

    print("=" * 60)
    print("Creating SFT Trainer")
    print("=" * 60)


    trainer = SFTTrainer(

        model=model,

        tokenizer=tokenizer,

        train_dataset=dataset,

        dataset_text_field="text",

        max_seq_length=TrainingConfig.MAX_SEQ_LENGTH,

        args=TrainingArguments(

            output_dir=TrainingConfig.OUTPUT_DIR,

            per_device_train_batch_size=
                TrainingConfig.BATCH_SIZE,


            gradient_accumulation_steps=
                TrainingConfig.GRADIENT_ACCUMULATION,


            learning_rate=
                TrainingConfig.LEARNING_RATE,


            num_train_epochs=
                TrainingConfig.NUM_EPOCHS,


            warmup_steps=
                TrainingConfig.WARMUP_STEPS,


            logging_steps=
                TrainingConfig.LOGGING_STEPS,


            save_steps=
                TrainingConfig.SAVE_STEPS,


            optim="adamw_8bit",

            fp16=False,

            bf16=False,

            report_to="none",

            seed=
                TrainingConfig.RANDOM_SEED,

        ),

    )


    print("✓ Trainer Created Successfully")


    return trainer
