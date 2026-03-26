from django.contrib import admin
from .models import Case, CaseDocument, Court


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ("name", "name_en", "order")
    list_editable = ("order",)
    search_fields = ("name", "name_en")


class CaseDocumentInline(admin.TabularInline):
    model = CaseDocument
    extra = 1
    fields = ("title", "file")


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("case_number", "client_name", "case_type", "court", "status", "filed_date", "created_at")
    list_filter = ("status", "case_type", "court", "filed_date")
    search_fields = ("case_number", "client_name", "description")
    date_hierarchy = "filed_date"
    list_per_page = 25
    list_editable = ("status",)
    inlines = [CaseDocumentInline]
    autocomplete_fields = ["court"]

    fieldsets = (
        ("मुद्दा जानकारी", {
            "fields": ("case_number", "client_name", "case_type", "court"),
        }),
        ("मिति र स्थिति", {
            "fields": ("filed_date", "status"),
        }),
        ("विस्तृत विवरण", {
            "fields": ("description", "notes"),
        }),
    )
