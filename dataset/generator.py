"""
Dataset Generator

Generates instruction tuning datasets for the
Container Intelligence Advisor.

Author: Tanuja Bhusal
"""

import json
import random
from pathlib import Path

from dataset.utils.profile_generator import ApplicationProfileGenerator
from dataset.core.scorer import RecommendationScorer
from dataset.core.selector import RecommendationSelector
from dataset.core.explainer import RecommendationExplainer


class DatasetGenerator:

    def __init__(self):

        self.profile_generator = ApplicationProfileGenerator()

        self.scorer = RecommendationScorer()

        self.selector = RecommendationSelector()

        self.instructions = (
            self.profile_generator
            .kb
            .instructions["instructions"]
        )

        self.output_dir = Path("dataset/output")

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ---------------------------------------------------------
    # Build Input
    # ---------------------------------------------------------

    def build_input(self, profile):

        return (
            f"Language: {profile.language}\n"
            f"Framework: {profile.framework}\n"
            f"Environment: {profile.environment}\n"
            f"Security: {profile.security}\n"
            f"Compliance: {profile.compliance}\n"
            f"Image Size: {profile.image_size}\n"
            f"Orchestrator: {profile.orchestrator}\n"
            f"Architecture: {profile.architecture}\n"
            f"Shell Required: {profile.shell_required}\n"
            f"Native Dependencies: {profile.native_dependencies}"
        )

    # ---------------------------------------------------------
    # Build Output
    # ---------------------------------------------------------

    def build_output(self, recommendation):

        reasons = "\n".join(
            f"- {reason}"
            for reason in recommendation.reasons
        )

        alternatives_text = ""

        if recommendation.alternatives:

            alternatives_text = (
                "\n\nAlternative Images:\n"
            )

            for index, alt in enumerate(
                recommendation.alternatives,
                start=1,
            ):

                alternatives_text += (
                    f"\n{index}. Registry: {alt['registry']}\n"
                    f"   Image: {alt['image']}\n"
                    f"   Reason: {alt['reason']}\n"
                )

        return (
            f"Recommended Registry: {recommendation.registry}\n"
            f"Recommended Image: {recommendation.image}\n"
            f"Variant: {recommendation.variant}\n"
            f"Confidence: {recommendation.confidence}%\n\n"
            f"Reasons:\n"
            f"{reasons}"
            f"{alternatives_text}"
        )

    # ---------------------------------------------------------
    # Build Dataset Record
    # ---------------------------------------------------------

    def build_record(
        self,
        profile,
        recommendation,
    ):

        return {

            "instruction": random.choice(
                self.instructions
            ),

            "input": self.build_input(
                profile
            ),

            "output": self.build_output(
                recommendation
            ),
        }

    # ---------------------------------------------------------
    # Generate Dataset
    # ---------------------------------------------------------

    def generate(
        self,
        samples=1000,
        filename="train.jsonl",
    ):

        output_file = self.output_dir / filename

        generated = 0

        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as f:

            while generated < samples:

                profile = self.profile_generator.generate()

                candidates = self.scorer.score(profile)

                if not candidates:
                    continue

                winner = self.selector.select(
                    candidates
                )

                top_candidates = candidates[:3]

                recommendation = RecommendationExplainer.explain(
                    profile,
                    winner,
                    top_candidates,
                )

                record = self.build_record(
                    profile,
                    recommendation,
                )

                f.write(
                    json.dumps(
                        record,
                        ensure_ascii=False,
                    )
                )

                f.write("\n")

                generated += 1

                if generated % 500 == 0:

                    print(
                        f"Generated {generated}/{samples} samples..."
                    )

        print("\n" + "=" * 60)
        print("Dataset Generation Complete")
        print(f"Output File : {output_file}")
        print(f"Samples     : {generated}")
        print("=" * 60)


if __name__ == "__main__":

    DatasetGenerator().generate(
        samples=1000,
        filename="train.jsonl",
    )
