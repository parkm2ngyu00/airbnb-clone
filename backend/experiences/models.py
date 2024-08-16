from django.db import models
from common.models import CommonModel

class Experience(CommonModel):

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    name = models.CharField(max_length=100)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100, null=True, blank=True)
    explanation = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name