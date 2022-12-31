from django.db import models


class Person(models.Model):
    register_data = models.DateField(auto_now=True)
    visitor_type = models.CharField(max_length=1)
    identification_type = models.CharField(max_length=2)
    identification = models.CharField(max_length=15, unique=True)
    fullname = models.CharField(max_length=300)

    def __str__(self):
        return self.fullname


class Register(models.Model):
    date = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    action = models.CharField(max_length=6)
    entry = models.CharField(max_length=50)

    def __str__(self):
        return self.person.fullname

