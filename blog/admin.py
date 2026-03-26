from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    readonly_fields = ("created_at",)
    list_filter = ("created_at",)
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    list_per_page = 20

    fieldsets = (
        ("विषयवस्तु", {
            "fields": ("title", "content", "thumbnail"),
            "description": "ब्लग लेखको मुख्य विषयवस्तु",
        }),
        ("अन्य जानकारी", {
            "fields": ("created_at",),
            "classes": ("collapse",),
            "description": "लेख सिर्जना गर्दा स्वचालित रूपमा सेट हुन्छ।",
        }),
    )
