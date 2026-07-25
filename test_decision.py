from agents.registry.dockerhub import DockerHubRegistryAgent
from agents.decision.decision_agent import DecisionAgent


registry = DockerHubRegistryAgent()

images = registry.search(
    "python",
    limit=5
)


decision = DecisionAgent()


best = decision.select_best(
    "python",
    images
)


print("Selected Image:")
print(best)
