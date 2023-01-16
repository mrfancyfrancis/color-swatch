from django.db import models

# Create your models here.


class Color(models.Model):
    choices = ['rgb', 'hsl']
    type = models.CharField(
        max_length=255,
        default="",
        blank=True,
        verbose_name="Type of Color Space",
    )
    input = models.JSONField(
        null=True,
        default=None,
        verbose_name="Input",
    )
