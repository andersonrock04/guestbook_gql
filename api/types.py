from graphene_django import DjangoObjectType
from .models import *


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = '__all__'


class RegisterType(DjangoObjectType):
    class Meta:
        model = Register
        fields = '__all__'

