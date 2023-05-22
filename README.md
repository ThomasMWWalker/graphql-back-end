# graphql-back-end
A basic implementation of a Django web applicaiton exposing a GraphQL endpoint at ```/graphql```. The implementation has been done with Python 3.10.8, with the requirements detailed in ```requirements.txt```.

## Admin access
A super user has been registered with the following credentials: 

*(Note it is not typical for a README to include credentials, but this is a demo app.)*

* Username: ```admin```

* Email: ```admin@admin.com```

* Password: ```admin```

## Testing

To run tests, execute the following command from the root directory of the project:

```python manage.py test```

## Running the server

To run the server, execute the following command from the root directory of the project:

```python manage.py runserver```

## GraphQL ```people``` Query

The ```people``` query returns a list of ```Person``` objects, with their email, name, and address.

```
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
```
