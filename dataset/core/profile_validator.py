"""
Profile Validator

Filters unrealistic application profiles.

Author: Tanuja Bhusal
"""

from dataset.core.models import ApplicationProfile


class ProfileValidator:

    @staticmethod
    def is_valid(profile: ApplicationProfile):

        # OpenShift is typically used for enterprise workloads
        if (
            profile.orchestrator == "OpenShift"
            and profile.compliance == "None"
        ):
            return False

        # High security production usually implies enterprise
        if (
            profile.environment == "Production"
            and profile.security == "High"
            and profile.compliance == "None"
        ):
            return False

        return True
