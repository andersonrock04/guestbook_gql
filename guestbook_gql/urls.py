from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from api.schema import schema
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie


urlpatterns = [
    path('guestbook/', csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True, schema=schema)))),
    path('admin/', admin.site.urls),
]
