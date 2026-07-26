class PromptBuilder:

    @staticmethod
    def build(profile):

        return f"""
### Instruction:
Recommend the best Docker base image.

### Input:
Language: {profile["language"]}
Framework: {profile["framework"]}
Environment: {profile["environment"]}
Security: {profile["security"]}
Compliance: {profile["compliance"]}
Image Size: {profile["image_size"]}
Orchestrator: {profile["orchestrator"]}
Architecture: {profile["architecture"]}
Shell Required: {profile["shell_required"]}
Native Dependencies: {profile["native_dependencies"]}

### Response:
"""
