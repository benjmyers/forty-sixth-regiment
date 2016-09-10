from django.db import models

class Soldier(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=5)
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.company