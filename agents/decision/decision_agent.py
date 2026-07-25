"""
Decision Agent

Combines model recommendation
with registry results.

Author:
Tanuja Bhusal
"""


class DecisionAgent:


    def select_best(
        self,
        recommendation,
        registry_images,
    ):


        if not registry_images:
            return None


        scores = []


        for image in registry_images:

            score = 0


            name = image.name.lower()


            # Python match
            if recommendation.lower() in name:
                score += 10


            # Official image preference
            if name == recommendation.lower():
                score += 20


            # Docker official images
            if "/" not in name:
                score += 10


            scores.append(
                (
                    score,
                    image
                )
            )


        scores.sort(
            key=lambda x: x[0],
            reverse=True
        )


        return scores[0][1]
