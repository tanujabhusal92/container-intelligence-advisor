from dataset.core.models import ApplicationProfile
from dataset.core.scorer import RecommendationScorer
from dataset.core.selector import RecommendationSelector

profile = ApplicationProfile(
    language="Python",
    framework="FastAPI",
    environment="Production",
    security="High",
    compliance="Enterprise",
    image_size="Small",
    orchestrator="Kubernetes",
    architecture="amd64",
    shell_required=False,
    native_dependencies=False,
)

scorer = RecommendationScorer()

candidates = scorer.score(profile)

print("\n===== Candidates =====")

for candidate in candidates:
    print(
        f"{candidate.id:20} "
        f"{candidate.registry:12} "
        f"Score={candidate.score}"
    )

best = RecommendationSelector.select(candidates)

print("\n===== Winner =====")

print(best)
