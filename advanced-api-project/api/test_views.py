"""Testing your CRUD API here"""

# To write the test I first of all import the in built django testing module to be inherited from

#Ask mentor Nehemiah why and how the test db can be setup/configured
from rest_framework.test import APITestCase
from .models import Book
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

class BookTests(APITestCase):
    def setUp(self):
        #Create the user for authentication
        User = get_user_model()
        user = User.objects.create_user(username="testuser", password="testpass")
       
        #Log user in
        login_successful = self.client.login(username="testuser", password="testpass")

        #Debug print as to whether it was succesful
        print("Login successful", login_successful)
        
        self.book_data = {'title': 'Last Days at Forcados', 'publication_year': 2017}
    print("Setting test environment...")

    #Creating a book instance apiendpoint with post, test. 
    def test_create_book(self):
        """
        Ensures books can be created and saved
        """        
        url = reverse("book-create",)
        response = self.client.post(url, self.book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)        #Book instance properly saved and populated the database
        print()

    #Updating book api endpoint with get, put, and patch test
    def test_update_book(self):
        """
        Ensures books can be updated totally or partially
        """
        #First of all create the book instance
        book = Book.objects.create(**self.book_data)       
        
        #Set the request url to get the book update url
        #using the book's primary key
        url = reverse("books-update", kwargs={"pk": book.pk})
         
        #Define the updated book data
        put_updated_book_data = {"title": "The last straw", "publication_year": 2025}
        response = self.client.put(url,  put_updated_book_data, format="json")

        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)

        #Define the partially updated book data
        patch_updated_book_data = {"publication_year": 2017}
        response = self.client.patch(url, patch_updated_book_data, format="json")

        #Prints to check the status code before use in the assertions
        #Debugging prints
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], put_updated_book_data["title"])
        self.assertEqual(response.data["publication_year"], patch_updated_book_data["publication_year"])      

    #Deleting a book instance apiendpoint with delete, tests.
    def test_delete_book(self):
        #The setup already holds a book data so I can just create an instance from it

        #Step 1: Create a book instance

        book = Book.objects.create(**self.book_data)

        #Step 2: Define the url for drf to get the delete url
        # Using it's primary key      
        url = reverse("book-delete", kwargs={"pk": book.pk})

        
        #Step 3: Delete the book instance
        response = self.client.delete(url, self.book_data, format="json")

        print("Response Status Code", response.status_code)
        print("Response Data", response.data)
        

        # Tests
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT),
        self.assertIsNone(response.data)    #Checks that the request returns back None(Nothing)