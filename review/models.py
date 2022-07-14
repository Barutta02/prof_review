from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator

# Create your models here.
class Review(models.Model):
    nome = models.CharField(max_length = 20)
    cognome = models.CharField(max_length = 25)
    descrizione = models.TextField(max_length = 360)
    stelle = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.nome + " " + self.cognome