from django.db import models


# Create your models here.
class Donor(models.Model):
    blood_group = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)
    when_needed = models.DateTimeField()
    contact_number = models.IntegerField(max_length=11)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.blood_group
