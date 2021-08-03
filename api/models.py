from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=250)
    def __str__(self):
        return self.name
# class Div(models.Model):
#     standerd=models.IntegerField()
#     division=models.CharField(max_length=120)
#     shift=models.CharField(max_length=120)
#     def __str__(self):
#         return self.standerd