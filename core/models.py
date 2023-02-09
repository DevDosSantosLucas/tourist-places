from django.db import models
from attractions.models import attraction
from comments.models import comment
from assessments.models import assessment 
from localization.models import localization

class IdentificationDoc(models.Model):
    description = models.CharField(max_length=100)

class tourist_places(models.Model):
    name = models.CharField( max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)

    attractions = models.ManyToManyField(attraction)
    comments = models.ManyToManyField(comment)
    assessments = models.ManyToManyField(assessment)
    address = models.ForeignKey(localization, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='tourist_places', null=True, blank=True)
    identification_document = models.OneToOneField(
        IdentificationDoc,on_delete = models.CASCADE, null=True,blank=True)

    @property
    def full_description2(self):
        return '%s - %s' % (self.name,self.description)




    def __str__(self):
        return self.name
