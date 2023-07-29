from django.contrib.gis.db import models
from django.contrib.postgres.search import SearchVectorField, SearchVector


class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    search_vector = SearchVectorField(null=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('name', 'description')
        super(Place, self).save(*args, **kwargs)