from django.db import models


class Department(models.Model):

    name = models.CharField(max_length=100)
    budget = models.FloatField(max_length=100)

    def __str__(self):
        return f"{self.name} with a budget of ${self.budget}"
