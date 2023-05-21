from django.contrib import admin
from .models import Person, Address

# Registering models to create Admin views
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'street', 'city', 'state')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'address')

