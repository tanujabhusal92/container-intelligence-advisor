"""
QLoRA Training Pipeline

Main entry point for Container Intelligence Advisor.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""


from trainer.model_loader import load_model
from trainer.lora import apply_lora
from trainer.dataset_loader import load_training_dataset
from trainer.formatter import format_dataset
from trainer.trainer_builder import create_trainer
from trainer.saver import save_model



def main():

    print("=" * 60)
    print("Container Intelligence Advisor")
    print("QLoRA Training Started")
    print("=" * 60)


    # 1. Load Base Model

    model, tokenizer = load_model()



    # 2. Apply LoRA Adapter

    model = apply_lora(
        model
    )



    # 3. Load Dataset

    dataset = load_training_dataset()



    # 4. Format Dataset

    dataset = format_dataset(
        dataset
    )



    # 5. Create Trainer

    trainer = create_trainer(

        model,

        tokenizer,

        dataset,

    )



    # 6. Start Training

    print("=" * 60)
    print("Starting Model Training")
    print("=" * 60)


    trainer.train()



    # 7. Save Adapter

    save_model(

        model,

        tokenizer,

    )


    print("=" * 60)
    print("Training Completed Successfully")
    print("=" * 60)



if __name__ == "__main__":

    main()
