from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField("शीर्षक", max_length=255)
    content = RichTextField("विषयवस्तु")
    thumbnail = models.ImageField("थम्बनेल", upload_to="thumbnails/", null=True, blank=True)
    created_at = models.DateTimeField("प्रकाशन मिति", auto_now_add=True)

    class Meta:
        verbose_name = "ब्लग लेख"
        verbose_name_plural = "ब्लग लेखहरू"

    def __str__(self):
        return self.title

