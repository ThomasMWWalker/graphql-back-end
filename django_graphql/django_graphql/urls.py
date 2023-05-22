from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

from person.schema import schema as person_schema # import the Person schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=person_schema)), # register the GraphQL endpoint view
]
