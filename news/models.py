from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.name
