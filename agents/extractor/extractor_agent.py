"""
Recommendation Extractor Agent

Extracts the image search term from
LLM generated recommendations.

Author: Tanuja Bhusal
Project: Container Intelligence Advisor
"""

import re


class RecommendationExtractorAgent:

    def extract(
        self,
        response: str,
    ) -> dict:

        response = response.lower()

        result = {
            "search_term": None,
        }

        patterns = [

            r"recommended image:\s*([^\n]+)",

            r"recommended registry:.*?\nrecommended image:\s*([^\n]+)",

            r"use\s+`([^`]+)`",

            r"use the\s+([^\s]+)",

            r"`([^`]+)`",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                response,
                re.MULTILINE,
            )

            if match:

                image = (
                    match
                    .group(1)
                    .strip()
                )

                image = image.split(":")[0]

                result["search_term"] = image

                return result

        #
        # Language fallback
        #

        language_map = {

            "python": "python",

            "java": "eclipse-temurin",

            "node": "node",

            "golang": "golang",

            "go": "golang",

            ".net": "dotnet",

            "dotnet": "dotnet",
        }

        for language, image in language_map.items():

            if language in response:

                result["search_term"] = image

                return result

        result["search_term"] = "docker"

        return result
