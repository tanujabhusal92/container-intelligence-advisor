"""
Inference Test

Loads base model + LoRA adapter
and generates container recommendations.

Author: Tanuja Bhusal
"""


from unsloth import FastLanguageModel
from peft import PeftModel

from training.config import TrainingConfig



# -------------------------------
# Load Base Model
# -------------------------------

print("Loading base model...")


model, tokenizer = FastLanguageModel.from_pretrained(

    model_name=TrainingConfig.MODEL_NAME,

    max_seq_length=TrainingConfig.MAX_SEQ_LENGTH,

    load_in_4bit=True,

)



# -------------------------------
# Load LoRA Adapter
# -------------------------------

print("Loading LoRA adapter...")


model = PeftModel.from_pretrained(

    model,

    TrainingConfig.OUTPUT_DIR,

)



# -------------------------------
# Enable inference mode
# -------------------------------

FastLanguageModel.for_inference(
    model
)



# -------------------------------
# Test Prompt
# -------------------------------


prompt = """
### Instruction:
Recommend the best container base image.

### Input:
Language: Python
Framework: FastAPI
Environment: Production
Security: High
Compliance: Enterprise
Image Size: Small
Orchestrator: Kubernetes
Architecture: amd64
Shell Required: False
Native Dependencies: True

### Response:
"""


inputs = tokenizer(

    prompt,

    return_tensors="pt",

).to("cuda")



# -------------------------------
# Generate Response
# -------------------------------


outputs = model.generate(

    **inputs,

    max_new_tokens=200,

    temperature=0.7,

)



response = tokenizer.decode(

    outputs[0],

    skip_special_tokens=True,

)


print("=" * 60)

print(response)

print("=" * 60)
