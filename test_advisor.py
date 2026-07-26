from agents.advisor.advisor_agent import (
    ContainerAdvisorAgent,
)


llm_response = """
Recommended Registry: docker

Recommended Image: python

Reasons:
- Production ready
- Kubernetes compatible
"""


advisor = ContainerAdvisorAgent()


result = advisor.recommend(
    llm_response
)


print(result)
