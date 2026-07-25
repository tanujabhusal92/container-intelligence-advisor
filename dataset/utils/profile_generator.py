"""
Application Profile Generator

Generates realistic application profiles for training.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

import random

from dataset.core.loader import KnowledgeBase
from dataset.core.models import ApplicationProfile


class ApplicationProfileGenerator:

    def __init__(self):

        self.kb = KnowledgeBase().load()

        # Generate profiles only for languages that have
        # at least one image defined in images.yaml
        self.supported_languages = sorted(
            {
                image["language"]
                for image in self.kb.images["images"]
            }
        )

    def generate(self):

        language = random.choice(
            self.supported_languages
        )

        framework = random.choice(
            self.kb.frameworks[language]["frameworks"]
        )

        return ApplicationProfile(

            language=language,

            framework=framework,

            environment=random.choice([
                "Production",
                "Development"
            ]),

            security=random.choice([
                "Low",
                "Medium",
                "High"
            ]),

            compliance=random.choice([
                "None",
                "Enterprise"
            ]),

            image_size=random.choice([
                "Small",
                "Balanced",
                "Performance"
            ]),

            orchestrator=random.choice([
                "Docker",
                "Kubernetes",
                "OpenShift"
            ]),

            architecture=random.choice([
                "amd64",
                "arm64"
            ]),

            shell_required=random.choice([
                True,
                False
            ]),

            native_dependencies=random.choice([
                True,
                False
            ]),
        )


if __name__ == "__main__":

    generator = ApplicationProfileGenerator()

    print("Supported Languages:")
    print(generator.supported_languages)

    print("\nSample Profiles:\n")

    for _ in range(5):
        print(generator.generate())
