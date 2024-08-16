from django.db import models

class CommonModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # DB에 추가하지 않음
    class Meta:

        abstract = True