"""Testing your CRUD API here"""

"""
Step 2: Set Up Testing Environment
Configure Test Settings:
Use Django’s built-in test framework which is based on Python’s unittest module.
Configure a separate test database to avoid impacting your production or development data.

Step 3: Write Test Cases
Develop Test Scenarios:
Write tests that simulate API requests and check for correct status codes and response data. This includes:
Creating a Book and ensuring the data is correctly saved and returned.
Updating a Book and verifying the changes are reflected.
Deleting a Book and ensuring it is removed from the database.
Testing each endpoint with appropriate authentication and permission scenarios to ensure security controls are effective.



"""
#to write the test I first of all import the in built django testing module to be inherited from

#Ask mentor Nehemiah why and how the test db can be setup/configured
from rest_framework.test import APITestCase
from .models import Book
from rest_framework import status
from django.urls import reverse

#Write test here
class BookTests(APITestCase):
    def setUp(self):
        self.book_data = {'title': 'Last Days at Forcados', 'publication_year': 2017}
        print("Setting test environment...")

    def test_create_book(self):
        """
        Ensures books can be created and saved
        """        
        url = reverse("book-create")        #Finds the url path with the appropriate name automatically
        response = self.client.post("/api/books/create/", self.book_data, format='json')
        # response = self.client.post(url, self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)        #Book instance properly saved and populated the database
        print()
    

    
    def test_update_book(self):
        """
        Ensures books can be updated totally or partially
        """
        
        url = reverse("books-update", kwargs={"pk":1})
        response = self.client.put(url, self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        print("Testing DOne")
         
        