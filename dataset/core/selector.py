"""
Recommendation Selector

Chooses the highest-scoring image candidate.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from typing import List

from dataset.core.models import ImageCandidate


class RecommendationSelector:

    @staticmethod
    def select(candidates: List[ImageCandidate]):

        if not candidates:
            raise ValueError("No image candidates available.")

        return max(candidates, key=lambda c: c.score)
