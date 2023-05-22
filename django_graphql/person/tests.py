from django.test import TestCase
import json
from graphene_django.utils.testing import GraphQLTestCase

from .models import Person, Address # import the models we created
from .schema import schema


# Test the creation and attributes of an Address instance
class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(number=123, street='Test St', city='Test City', state='NSW')

    def test_address_creation(self):
        self.assertEqual(self.address.number, 123)
        self.assertEqual(self.address.street, 'Test St')
        self.assertEqual(self.address.city, 'Test City')
        self.assertEqual(self.address.state, 'NSW')


# Test the creation and attributes of a Person instance and the associated Address
class AddressPersonModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(number=123, street='Test St', city='Test City', state='NSW')
        self.person = Person.objects.create(email='test@email.com', name='Test Name', address=self.address)

    def test_person_creation(self):
        self.assertEqual(self.person.email, 'test@email.com')
        self.assertEqual(self.person.name, 'Test Name')
        self.assertEqual(self.person.address, self.address)


# Tests the functionality of the GraphQL endpoint, using the schema defined in .schema
class PeopleGraphQLTest(GraphQLTestCase):
    GRAPHQL_URL = '/graphql/'
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        self.address = Address.objects.create(number=123, street='Test St', city='Test City', state='NSW')
        self.person = Person.objects.create(email='test@email.com', name='Test Name', address=self.address)
    
    def test_people_query(self):

        # Define and execute a GraphQL query
        response = self.query(
            '''
            query {
                people {
                    email
                    name
                    address {
                        number
                        street
                        city
                        state
                    }
                }
            }
            '''
        )

        # Load the returned JSON data into a Python object
        content = json.loads(response.content)

        # Confirm that we get the expected data back
        self.assertResponseNoErrors(response)
        self.assertEqual(content['data']['people'][0]['email'], 'test@email.com')
        self.assertEqual(content['data']['people'][0]['name'], 'Test Name')
        self.assertEqual(content['data']['people'][0]['address']['number'], 123)
        self.assertEqual(content['data']['people'][0]['address']['street'], 'Test St')
        self.assertEqual(content['data']['people'][0]['address']['city'], 'Test City')
        self.assertEqual(content['data']['people'][0]['address']['state'], 'NSW')
