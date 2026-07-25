from agents.registry.dockerhub import DockerHubRegistryAgent


agent = DockerHubRegistryAgent()


results = agent.search(
    "python",
    limit=5
)


for image in results:

    print(
        image
    )
