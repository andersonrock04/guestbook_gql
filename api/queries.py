import graphene
from graphql_jwt.decorators import login_required
from .types import *
from .models import *


class Query(graphene.ObjectType):
    person = graphene.Field(PersonType, identification=graphene.String(required=True))

    @login_required
    def resolve_person(self, request, identification):
        try:
            return Person.objects.get(identification=identification)
        except Person.DoesNotExist:
            return Person.objects.none()

