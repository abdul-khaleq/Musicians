from django.db import models

# Create your models here.
class Musician(models.Model):
    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=12)
    instrumentType = models.CharField(max_length=55)

    def __str__(self) -> str:
        return f"Name: {self.firstName} {self.lastName}"
