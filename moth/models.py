from django.db import models

# Create your models here.


class Team_Member(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    service_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.service_type}"
