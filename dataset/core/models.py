"""
Data models for Container Intelligence Advisor.

These dataclasses represent the core objects used across
the recommendation engine.

Author: Tanuja Bhusal
"""

from dataclasses import dataclass, field
from typing import List, Dict


# ==========================================================
# User/Application Profile
# ==========================================================

@dataclass
class ApplicationProfile:

    language: str
    framework: str

    environment: str

    security: str

    compliance: str

    image_size: str

    orchestrator: str

    architecture: str

    shell_required: bool

    native_dependencies: bool


# ==========================================================
# Image Candidate
# ==========================================================

@dataclass
class ImageCandidate:

    id: str

    language: str

    registry: str

    image: str

    variants: Dict

    supports: Dict

    orchestrators: List[str]

    strengths: List[str]

    score: float = 0.0


# ==========================================================
# Recommendation
# ==========================================================

@dataclass
class Recommendation:

    registry: str

    image: str

    variant: str

    confidence: int

    score: float

    reasons: List[str] = field(default_factory=list)

    alternatives: list = field(default_factory=list)
