from inference.inference_service import (
    InferenceService,
)


service = InferenceService(

    base_model="unsloth/Llama-3.2-3B-Instruct",

    adapter_path="models/container-intelligence-advisor-lora",
)


prompt = """
### Instruction:
Recommend the best Docker base image.

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

print(
    service.generate(prompt)
)
