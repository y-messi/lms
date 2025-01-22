from django.db import models

# Create your models here.
class Student(models.Model):
    locker_number = models.PositiveIntegerField()
    user_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    enter_time = models.DateTimeField()
    exit_time = models.DateTimeField()
    
    def __str__(self):
        return f'{self.user_name}'
