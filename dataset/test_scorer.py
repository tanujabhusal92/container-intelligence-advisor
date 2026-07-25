from dataset.core.selector import RecommendationSelector
from dataset.core.scorer import RecommendationScorer
from dataset.core.models import ApplicationProfile

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

best = RecommendationSelector.select(candidates)

print(best)
