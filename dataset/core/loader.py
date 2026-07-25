"""
Knowledge Base Loader

Loads all YAML files from the knowledge_base directory and
provides a single interface for accessing them.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from pathlib import Path
import yaml


class KnowledgeBase:

    def __init__(self, kb_path=None):

        if kb_path is None:
            kb_path = (
                Path(__file__)
                .resolve()
                .parent
                .parent
                / "knowledge_base"
            )

        self.kb_path = kb_path

        self.languages = {}
        self.frameworks = {}
        self.registries = {}
        self.images = {}
        self.scoring = {}
        self.constraints = {}

    def _load_yaml(self, filename):

        file_path = self.kb_path / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Knowledge base file not found: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def load(self):

        self.languages = self._load_yaml("languages.yaml")

        self.frameworks = self._load_yaml("frameworks.yaml")

        self.registries = self._load_yaml("registries.yaml")

        self.images = self._load_yaml("images.yaml")

        self.scoring = self._load_yaml("scoring.yaml")

        self.constraints = self._load_yaml("constraints.yaml")

        return self

    def summary(self):

        print("=" * 60)

        print("Container Intelligence Advisor")

        print("=" * 60)

        print(f"Languages     : {len(self.languages.get('languages', []))}")

        print(f"Frameworks    : {len(self.frameworks)}")

        print(f"Registries    : {len(self.registries)}")

        print(f"Images        : {len(self.images.get('images', []))}")

        print("=" * 60)


if __name__ == "__main__":

    kb = KnowledgeBase().load()

    kb.summary()
