"""
Scoring Engine

Evaluates all compatible container images and assigns a score
based on the application profile and scoring rules.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from dataset.core.loader import KnowledgeBase
from dataset.core.models import ApplicationProfile, ImageCandidate


class RecommendationScorer:

    def __init__(self):

        self.kb = KnowledgeBase().load()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def score(self, profile: ApplicationProfile):

        candidates = []

        images = self.kb.images.get("images", [])

        for image in images:

            if image["language"] != profile.language:
                continue

            candidate = ImageCandidate(
                id=image["id"],
                language=image["language"],
                registry=image["registry"],
                image=image["image"],
                variants=image["variants"],
                supports=image["supports"],
                orchestrators=image["orchestrators"],
                strengths=image["strengths"],
            )

            candidate.score = self._calculate_score(
                candidate,
                profile,
            )

            candidates.append(candidate)

        candidates.sort(
            key=lambda x: x.score,
            reverse=True,
        )

        return candidates

    # ---------------------------------------------------------
    # Score Calculation
    # ---------------------------------------------------------

    def _calculate_score(
        self,
        candidate: ImageCandidate,
        profile: ApplicationProfile,
    ):

        score = 0

        score += self._registry_priority(candidate)

        score += self._security_score(
            candidate,
            profile,
        )

        score += self._enterprise_score(
            candidate,
            profile,
        )

        score += self._environment_score(
            candidate,
            profile,
        )

        score += self._shell_score(
            candidate,
            profile,
        )

        score += self._orchestrator_score(
            candidate,
            profile,
        )

        score += self._image_size_score(
            candidate,
            profile,
        )

        return score

    # ---------------------------------------------------------
    # Individual Rules
    # ---------------------------------------------------------

    def _registry_priority(self, candidate):

        registry = self.kb.registries.get(
            candidate.registry,
            {},
        )

        return registry.get("priority", 0)

    def _security_score(
        self,
        candidate,
        profile,
    ):

        if profile.security.lower() == "high":

            level = candidate.supports.get(
                "security",
                "",
            )

            if level == "very_high":
                return 35

            if level == "high":
                return 30

            if level == "medium":
                return 15

        return 0

    def _enterprise_score(
        self,
        candidate,
        profile,
    ):

        if profile.compliance.lower() != "enterprise":
            return 0

        if candidate.supports.get(
            "enterprise",
            False,
        ):
            return 40

        return 0

    def _environment_score(
        self,
        candidate,
        profile,
    ):

        env = profile.environment.lower()

        if env == "production":

            if "production" in candidate.variants:
                return 20

        if env == "development":

            if "development" in candidate.variants:
                return 20

        return 0

    def _shell_score(
        self,
        candidate,
        profile,
    ):

        shell = candidate.supports.get(
            "shell",
            False,
        )

        if profile.shell_required and shell:
            return 10

        if (not profile.shell_required) and (not shell):
            return 10

        return 0

    def _orchestrator_score(
        self,
        candidate,
        profile,
    ):

        if profile.orchestrator in candidate.orchestrators:
            return 15

        return 0

    def _image_size_score(
        self,
        candidate,
        profile,
    ):

        if profile.image_size.lower() != "small":
            return 0

        registry = candidate.registry

        if registry == "distroless":
            return 20

        if registry == "chainguard":
            return 20

        return 0
