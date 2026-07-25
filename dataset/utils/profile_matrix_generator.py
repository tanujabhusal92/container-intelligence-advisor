from itertools import product

from dataset.core.loader import KnowledgeBase
from dataset.core.models import ApplicationProfile
from dataset.core.profile_validator import ProfileValidator

class ProfileMatrixGenerator:

    def __init__(self):

        self.kb = KnowledgeBase().load()

        self.languages = sorted(
            {
                image["language"]
                for image in self.kb.images["images"]
            }
        )

    def generate(self):

        for language in self.languages:

            frameworks = self.kb.frameworks[language]["frameworks"]

            for values in product(

                frameworks,

                ["Production", "Development"],

                ["High", "Medium", "Low"],

                ["Enterprise", "None"],

                ["Small", "Balanced", "Performance"],

                ["Docker", "Kubernetes", "OpenShift"],

                ["amd64", "arm64"],

                [True, False],

                [True, False],

            ):

                profile = ApplicationProfile(

                    language=language,

                    framework=values[0],

                    environment=values[1],

                    security=values[2],

                    compliance=values[3],

                    image_size=values[4],

                    orchestrator=values[5],

                    architecture=values[6],

                    shell_required=values[7],

                    native_dependencies=values[8],
                )
                if ProfileValidator.is_valid(profile):
                    yield profile
