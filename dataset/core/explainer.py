"""
Recommendation Explainer

Generates human-readable explanations for why an image was
recommended.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from dataset.core.models import (
    ApplicationProfile,
    ImageCandidate,
    Recommendation,
)


class RecommendationExplainer:

    @staticmethod
    def explain(
        profile: ApplicationProfile,
        candidate: ImageCandidate,
        alternatives=None,
    ) -> Recommendation:

        reasons = []

        supports = candidate.supports

        # --------------------------------------------------
        # Enterprise
        # --------------------------------------------------

        if supports.get("enterprise", False):
            reasons.append(
                "Enterprise-supported container image."
            )

        # --------------------------------------------------
        # Security
        # --------------------------------------------------

        security = supports.get("security", "").lower()

        if security == "very_high":
            reasons.append(
                "Provides a minimal attack surface with very high security."
            )

        elif security == "high":
            reasons.append(
                "Designed for high-security production workloads."
            )

        elif security == "medium":
            reasons.append(
                "Suitable for general production deployments."
            )

        # --------------------------------------------------
        # FIPS
        # --------------------------------------------------

        if supports.get("fips", False):
            reasons.append(
                "Supports FIPS-compliant environments."
            )

        # --------------------------------------------------
        # Shell
        # --------------------------------------------------

        if profile.shell_required:

            if supports.get("shell", False):
                reasons.append(
                    "Includes shell utilities for debugging and administration."
                )

        else:

            if not supports.get("shell", True):
                reasons.append(
                    "No shell included, reducing attack surface."
                )

        # --------------------------------------------------
        # Native Dependencies
        # --------------------------------------------------

        if (
            profile.native_dependencies
            and supports.get("native_dependencies", False)
        ):
            reasons.append(
                "Supports applications requiring native libraries."
            )

        # --------------------------------------------------
        # Environment
        # --------------------------------------------------

        if (
            profile.environment.lower()
            in candidate.variants
        ):

            reasons.append(
                f"Optimized for {profile.environment.lower()} workloads."
            )

        # --------------------------------------------------
        # Orchestrator
        # --------------------------------------------------

        if (
            profile.orchestrator
            in candidate.orchestrators
        ):

            reasons.append(
                f"Compatible with {profile.orchestrator} deployments."
            )

        # --------------------------------------------------
        # Strengths from Knowledge Base
        # --------------------------------------------------

        for strength in candidate.strengths:
            if strength not in reasons:
                reasons.append(strength)

        # --------------------------------------------------
        # Confidence
        # --------------------------------------------------

        confidence = RecommendationExplainer._confidence(
            candidate.score
        )

        # --------------------------------------------------
        # Variant
        # --------------------------------------------------

        env = profile.environment.lower()

        variant = "latest"

        if env in candidate.variants:

            variant = candidate.variants[env][0]

        alternative_list = []

        if alternatives:

            for alt in alternatives:

                if alt.id == candidate.id:
                    continue

                alternative_list.append(
                    {
                        "registry": alt.registry,
                        "image": alt.image,
                        "reason": ", ".join(
                        alt.strengths[:2]
                         ),
                    }
                )    

        return Recommendation(
            registry=candidate.registry,
            image=candidate.image,
            variant=variant,
            confidence=confidence,
            score=candidate.score,
            reasons=reasons,
            alternatives=alternative_list,
        )

    @staticmethod
    def _confidence(score: float) -> int:

        if score >= 220:
            return 99

        if score >= 180:
            return 96

        if score >= 150:
            return 92

        if score >= 120:
            return 88

        return 80
