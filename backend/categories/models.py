from django.db import models
from common.models import CommonModel

class Category(CommonModel):

    class CategoryChoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = ("experiences", "Experiences")

    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=15, choices=CategoryChoices.choices, default=CategoryChoices.ROOMS)

    def __str__(self) -> str:
        return self.name
    

    class Meta:

        verbose_name_plural = "Categories"