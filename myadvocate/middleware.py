from django.utils import translation


class AdminNepaliMiddleware:
    """
    Activates Nepali language for admin portal URLs so the lawyer
    sees labels in Nepali (मुद्दा नम्बर, etc.) when adding cases and blogs.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin/"):
            translation.activate("ne")
            request.LANGUAGE_CODE = "ne"

        response = self.get_response(request)

        if request.path.startswith("/admin/"):
            translation.deactivate()

        return response
