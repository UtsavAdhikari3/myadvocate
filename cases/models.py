from django.db import models


class Court(models.Model):
    """अदालत - Courts that can be selected when adding a case."""
    name = models.CharField("अदालतको नाम", max_length=255)
    name_en = models.CharField("अदालतको नाम (अङ्ग्रेजी)", max_length=255, blank=True, help_text="Optional English name")
    order = models.PositiveIntegerField("क्रम", default=0, help_text="Display order in dropdown")

    class Meta:
        verbose_name = "अदालत"
        verbose_name_plural = "अदालतहरू"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Case(models.Model):
    STATUS_CHOICES = [
        ("pending", "पेन्डिङ"),
        ("ongoing", "चलिरहेको"),
        ("closed", "बन्द"),
    ]
    CASE_TYPE_CHOICES = [
        ("criminal", "फौजदारी"),
        ("civil", "दीवानी"),
        ("family", "पारिवारिक"),
        ("corporate", "कर्पोरेट"),
        ("other", "अन्य"),
    ]

    case_number = models.CharField("मुद्दा नम्बर", max_length=50, unique=True)
    client_name = models.CharField("ग्राहकको नाम", max_length=255)
    case_type = models.CharField("मुद्दाको प्रकार", max_length=20, choices=CASE_TYPE_CHOICES)
    court = models.ForeignKey(
        Court,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="अदालत",
        related_name="cases",
    )
    filed_date = models.DateField("दाखिल मिति", null=True, blank=True)
    status = models.CharField("स्थिति", max_length=20, choices=STATUS_CHOICES, default="pending")
    description = models.TextField("विवरण", blank=True)
    notes = models.TextField("नोटहरू", blank=True)
    created_at = models.DateTimeField("सिर्जना मिति", auto_now_add=True)
    updated_at = models.DateTimeField("अद्यावधिक मिति", auto_now=True)

    class Meta:
        verbose_name = "मुद्दा"
        verbose_name_plural = "मुद्दाहरू"

    def __str__(self):
        return f"{self.case_number} — {self.client_name}"


class CaseDocument(models.Model):
    """मुद्दा सम्बन्धी कागजात - Documents/files attached to a case."""
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        verbose_name="मुद्दा",
        related_name="documents",
    )
    title = models.CharField("कागजातको नाम", max_length=255, blank=True)
    file = models.FileField("फाइल", upload_to="case_documents/%Y/%m/")
    uploaded_at = models.DateTimeField("अपलोड मिति", auto_now_add=True)

    class Meta:
        verbose_name = "मुद्दाको कागजात"
        verbose_name_plural = "मुद्दाका कागजातहरू"
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title or self.file.name
