from agents.extractor.extractor_agent import (
    RecommendationExtractorAgent,
)


response = """
Recommended Registry: docker

Recommended Image: python

Reasons:
- Production ready
"""


agent = RecommendationExtractorAgent()

print(
    agent.extract(response)
)
