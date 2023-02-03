from django.db import models
from attractions.models import attraction
from comments.models import comment
from assessments.models import assessment 
from localization.models import localization

class tourist_places(models.Model):
    name = models.CharField( max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)

    attractions = models.ManyToManyField(attraction)
    comments = models.ManyToManyField(comment)
    assessments = models.ManyToManyField(assessment)
    address = models.ForeignKey(localization, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name
