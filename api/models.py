from django.db import models
from django.contrib.auth.models import User


class Guard (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.user.username


class Person (models.Model):
    register_date = models.DateField(auto_now=True)
    visitor_type = models.CharField(max_length=2)
    identification_type = models.CharField(max_length=3)
    identification = models.CharField(max_length=15, unique=True)
    fullname = models.CharField(max_length=300)

    def __str__ (self):
        return self.fullname


class Register (models.Model):
    register_date = models.DateTimeField(auto_now=True)
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    action = models.CharField(max_length=6)
    entry = models.CharField(max_length=50)

    def __str__ (self):
        return self.person.fullname

