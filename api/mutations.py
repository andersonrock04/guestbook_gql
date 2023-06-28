import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required
from django.contrib.auth.models import User
from .types import *
from .models import *


class PersonMutation (graphene.Mutation):
    person = graphene.Field(PersonType)

    class Arguments:
        visitor_type = graphene.String(required=True)
        identification_type = graphene.String(required=True)
        identification = graphene.String(required=True)
        fullname = graphene.String(required=True)

    @classmethod
    @login_required
    def mutate (cls, self, request, visitor_type, identification_type, identification, fullname):
        person = Person.objects.create(visitor_type=visitor_type, identification_type=identification_type, identification=identification, fullname=fullname)
        return cls(person=person)

class PersonUpdate (graphene.Mutation):
    person = graphene.Field(PersonType)

    class Arguments:
        visitor_type = graphene.String()
        identification_type = graphene.String()
        identification = graphene.String(required=True)
        fullname = graphene.String()

    @classmethod
    @login_required
    def mutate (cls, self, request, **kwargs):
        try:
            person = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return Person.objects.none()
        if kwargs['visitor_type']:
            person.visitor_type = kwargs['visitor_type']
        if kwargs['identification_type']:
            person.identification_type = kwargs['identification_type']
        if kwargs['identification']:
            person.identification = kwargs['identification']
        if kwargs['fullname']:
            person.fullname = kwargs['fullname']
        person.save()
        return cls(person=person)

class PersonDelete (graphene.Mutation):
    deleted = graphene.Boolean()

    class Arguments:
        identification = graphene.String(required=True)

    @classmethod
    @login_required
    def mutate (cls, self, identification):
        try:
            Person.objects.get(identification=identification).delete()
        except Person.DoesNotExist:
            return cls(deleted=False)
        return cls(deleted=True)


class RegisterMutation (graphene.Mutation):
    register = graphene.Field(RegisterType)

    class Arguments:
        identification = graphene.String(required=True)
        action = graphene.String(required=True)
        entry = graphene.String(required=True)

    @classmethod
    @login_required
    def mutate (cls, self, request, identification, action, entry):
        try:
            person = Person.objects.get(identification=identification)
        except Person.DoesNotExist:
            return cls(register=Register.objects.none())
        register = Register.objects.create(person=person, action=action, entry=entry)
        return cls(register=register)

class RegisterDelete (graphene.Mutation):
    deleted = graphene.Boolean()

    class Arguments:
        identification = graphene.String(required=True)

    @classmethod
    @login_required
    def mutate (cls, self, request, identification):
        try:
            Register.objects.get(identification=identification).delete()
        except Register.DoesNotExist:
            return cls(deleted=False)
        return cls(deleted=True)


class Mutation (graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    create_person = PersonMutation.Field()
    update_person = PersonUpdate.Field()
    delete_person = PersonDelete.Field()

    create_register = RegisterMutation.Field()
    delete_register = RegisterDelete.Field()

