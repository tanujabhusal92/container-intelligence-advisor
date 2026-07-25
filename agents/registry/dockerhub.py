"""
Docker Hub Registry Agent

Searches Docker Hub for container images.

Author: Tanuja Bhusal
"""


import requests

from agents.registry.models import RegistryImage



class DockerHubRegistryAgent:


    BASE_URL = (
        "https://hub.docker.com/v2/search/repositories"
    )


    def search(
        self,
        query,
        limit=5,
    ):

        params = {
            "query": query,
            "page_size": limit,
        }


        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=10,
        )


        response.raise_for_status()


        data = response.json()


        images = []


        for item in data.get(
            "results",
            []
        ):


            images.append(

                RegistryImage(

                    registry="docker.io",

                    name=item["repo_name"],

                    tag="latest",

                    description=item.get(
                        "short_description",
                        ""
                    ),

                    security="unknown",

                    size="unknown",
                )

            )


        return images
