from django.db import models

from colors.utils import random_type, random_percentage, \
                         random_byte, random_number
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

    def generate_random_color(self):
        import json

        color_type = random_type()
        input = ''
        if color_type == 'rgb':
            red = random_byte()
            green = random_byte()
            blue = random_byte()
            input = {
                'type': color_type,
                red: red,
                green: green,
                blue: blue
            }
        elif color_type == 'hsl':
            hue = random_number(max=360)
            saturation = random_percentage()
            lightness = random_percentage()
            input = {
                'type': color_type,
                hue: hue,
                saturation: saturation,
                lightness: lightness
            }

        return Color(type=color_type, input=json.dumps(input))
