from dataset.utils.profile_generator import (
    ApplicationProfileGenerator
)

generator = ApplicationProfileGenerator()

for i in range(5):

    profile = generator.generate()

    print(profile)
