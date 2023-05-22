from django.db import models
import graphene


class AustralianStateEnum(graphene.Enum):
    '''
    Enumeration of Australian states for the Address model
    '''

    NSW = 'New South Wales'
    VIC = 'Victoria'
    QLD = 'Queensland'
    SA = 'South Australia'
    WA = 'Western Australia'
    TAS = 'Tasmania'
    NT = 'Northern Territory'
    ACT = 'Australian Capital Territory'


class Address(models.Model):
    '''
    Address model to store information about an address
    '''

    STATE_CHOICES = [(state.name, state.value) for state in AustralianStateEnum]

    # Fields
    number = models.IntegerField()
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)

    class Meta:
        verbose_name_plural = 'adresses'  # Specify the plural name for Django backend

    def __str__(self) -> str:
        '''
        String representation of an address instance
        '''
        return f'{self.number} {self.street}, {self.city}, {self.state}'


class Person(models.Model):
    '''
    Person model to store information about a person
    '''

    # Fields
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE) # one person has one address

    class Meta:
        verbose_name_plural = 'people'  # Specify the plural name for Django backend

    def __str__(self) -> str:
        '''
        String representation of an person instance
        '''
        return f'{self.email}, {self.name}'
    