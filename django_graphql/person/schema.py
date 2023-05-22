import graphene
from graphene_django import DjangoObjectType # DjangoObjectType allows us to map Django models to GraphQL types

from .models import Person, Address # import the models we created


# Create GraphQL types for each model
class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


# Create a Query class to define the GraphQL query (the read operations)
class Query(graphene.ObjectType):
    # Creating a 'people' field of type list of PersonType.
    # This means when the 'people' field is queried, it will return a list of PersonType objects.
    people = graphene.List(PersonType)

    # Define the resolver function for the people field
    # The resolver function is responsible for querying the database and returning the data
    # We are using select_related() to perform a join between the Person and Address tables to improve performance
    def resolve_people(self, info):
        return Person.objects.select_related('address').all()


# Create a schema for the query
schema = graphene.Schema(query=Query)
