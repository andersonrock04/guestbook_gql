from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from api.schema import schema
from graphene_django.views import GraphQLView



urlpatterns = [
    path('guestbook/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    path('admin/', admin.site.urls),
]
