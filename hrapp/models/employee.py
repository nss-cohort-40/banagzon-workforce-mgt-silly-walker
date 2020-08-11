from django.db import models
from .department import Department


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField()
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, default=1)
    is_supervisor = models.BooleanField()

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})
