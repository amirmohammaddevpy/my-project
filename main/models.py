from django.db import models

# Create your models here.
class MyProject(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/project")
    descriptions = models.TextField()
    link_site = models.URLField()
    link_project = models.URLField()
    viede_site = models.FileField(upload_to="videos/project")
    
    def __str__(self):
        return self.name