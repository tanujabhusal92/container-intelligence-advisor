from dataset.core.models import ApplicationProfile
from dataset.core.scorer import RecommendationScorer
from dataset.core.selector import RecommendationSelector
from dataset.core.explainer import RecommendationExplainer


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

winner = RecommendationSelector.select(candidates)

recommendation = RecommendationExplainer.explain(
    profile,
    winner,
)

print("=" * 60)
print("FINAL RECOMMENDATION")
print("=" * 60)

print(f"Registry   : {recommendation.registry}")
print(f"Image      : {recommendation.image}")
print(f"Variant    : {recommendation.variant}")
print(f"Confidence : {recommendation.confidence}%")
print(f"Score      : {recommendation.score}")

print("\nReasons:")

for reason in recommendation.reasons:
    print(f"  ✓ {reason}")
