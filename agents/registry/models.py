"""
Registry Agent Models

Author: Tanuja Bhusal
"""


from dataclasses import dataclass


@dataclass
class RegistryImage:

    registry: str

    name: str

    tag: str

    description: str

    security: str

    size: str
