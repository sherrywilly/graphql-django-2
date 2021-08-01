from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
# from graphql.type import schema
from cookbook.schema import schema as Schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',GraphQLView.as_view(graphiql=True,schema=Schema))
]

