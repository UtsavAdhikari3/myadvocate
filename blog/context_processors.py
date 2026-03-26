from datetime import datetime


def site_context(request):
    """Add common template variables across the site."""
    return {
        "now": datetime.now(),
    }
