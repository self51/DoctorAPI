from django.db import models


class Direction(models.Model):
    name_direction = models.CharField(blank=True, max_length=30)
    slug = models.SlugField(max_length=40)
    sort_number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name_direction


class Doctor(models.Model):
    name = models.CharField(blank=True, max_length=30)
    slug = models.SlugField(max_length=40)
    directions = models.ManyToManyField(
        Direction,
        related_name="directions",
        related_query_name="direction",
    )
    description = models.CharField(blank=True, max_length=200)
    birth_date = models.DateField(max_length=8)
    experience = models.IntegerField(default=0)
    sort_number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name
