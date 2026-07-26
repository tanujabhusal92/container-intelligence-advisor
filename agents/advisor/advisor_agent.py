"""
Container Advisor Agent

Coordinates all agents to generate
a validated container image recommendation.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

from agents.extractor.extractor_agent import (
    RecommendationExtractorAgent,
)

from agents.registry.dockerhub import (
    DockerHubRegistryAgent,
)

from agents.decision.decision_agent import (
    DecisionAgent,
)


class ContainerAdvisorAgent:

    def __init__(self):

        self.extractor = RecommendationExtractorAgent()

        self.registry = DockerHubRegistryAgent()

        self.decision = DecisionAgent()

    def recommend(
        self,
        llm_response,
    ):

        #
        # Step 1
        #

        extracted = self.extractor.extract(
            llm_response
        )

        search_term = extracted["search_term"]

        #
        # Step 2
        #

        registry_results = self.registry.search(
            search_term,
            limit=5,
        )

        #
        # Step 3
        #

        best = self.decision.select_best(
            search_term,
            registry_results,
        )

        #
        # Step 4
        #

        return {

            "llm_recommendation": search_term,

            "recommended_registry": best.registry,

            "recommended_image": best.name,

            "recommended_tag": best.tag,

            "description": best.description,

            "security": best.security,

            "size": best.size,

            "alternative_images": [

                {   
                    "registry": image.registry,
                    "image": image.name,
                    "tag": image.tag,
                    "description": image.description,
                }

                for image in registry_results
            ],
        }   
