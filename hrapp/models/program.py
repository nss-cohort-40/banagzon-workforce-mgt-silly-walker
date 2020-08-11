from django.db import models


class Program(models.Model):

    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.title} has a start date of {self.start_date} and end date of {self.end_date}. Only {self.capacity} people can attend"
