from django.db import models

# Create your models here.
class Temperatures(models.Model):
    date = models.DateField("Date Created", auto_now_add=True)
    time = models.TimeField("Time Created", auto_now_add=True)
    burnerzone = models.IntegerField("BunerZone")
    burner_1 = models.IntegerField("Temperature")
    burner_2 = models.IntegerField("Temperature")
    burner_3 = models.IntegerField("Temperature")
    burner_4 = models.IntegerField("Temperature")
    burner_5 = models.IntegerField("Temperature")
    burner_6 = models.IntegerField("Temperature")
    burner_7 = models.IntegerField("Temperature")
    burner_8 = models.IntegerField("Temperature")
    burner_9 = models.IntegerField("Temperature")
    burner_10 = models.IntegerField("Temperature")
    burner_11 = models.IntegerField("Temperature")
    burner_12 = models.IntegerField("Temperature")
    user = models.CharField("User", max_length=30)

    def __str__(self):
        return str(self.date)