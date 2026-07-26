"""
Inference Service

Loads the fine-tuned model and generates
recommendations.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

import torch

from unsloth import FastLanguageModel

from peft import PeftModel


class InferenceService:

    def __init__(
        self,
        base_model,
        adapter_path,
        max_seq_length=2048,
    ):

        print("Loading base model...")

        self.model, self.tokenizer = (
            FastLanguageModel.from_pretrained(
                model_name=base_model,
                max_seq_length=max_seq_length,
                load_in_4bit=True,
            )
        )

        print("Loading LoRA adapter...")

        self.model = PeftModel.from_pretrained(
            self.model,
            adapter_path,
        )

        FastLanguageModel.for_inference(
            self.model
        )

        print("Inference service ready.")

    def generate(
        self,
        prompt,
        max_new_tokens=200,
    ):

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
        ).to("cuda")

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            do_sample=False,
        )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True,
        )
