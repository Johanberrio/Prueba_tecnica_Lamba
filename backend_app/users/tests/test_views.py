from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginViewTest(APITestCase):
    def setUp(self):
        self.login_url = "/api/login/"  # Cambia esta URL si es necesario
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_login_success(self):
        """Prueba de inicio de sesión exitoso."""
        data = {"username": "testuser", "password": "password123"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["username"], "testuser")
       

    def test_login_invalid_credentials(self):
        """Prueba de inicio de sesión con credenciales inválidas."""
        data = {"username": "testuser", "password": "wrongpassword"}
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("non_field_errors", response.data)

class RegisterViewTest(APITestCase):
    
    def setUp(self):
        # register's endpoint URL
        self.register_url = "/api/register/" 

    def test_register_success(self):
        data = {'username': 'new_user',
                'password': 'password',  
                'name': 'test',
                'age': 20,
                'gender': 'M',  
                'cc': '2',
                'phone': '222',
                'email': 'newuser@example.com'}
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_register_missing_data(self):
        """Test of registration with missing data (user name)."""
        data = {
            "password": "password123",
            "email": "testuser@example.com"
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data) # missing username error

    def test_register_duplicate_username(self):
        """Test registration with a duplicate user name."""
        # First register the user
        data1 = {
            "username": "testuser",
            "name": "test",
            "age": "20",
            "gender": "M",
            "password": "password123",
            "cc": "2",
            "phone": "222",
            "email": "testuser@example.com"
        }
        self.client.post(self.register_url, data1)
        
        # Then, try to register another user with the same username
        data2 = {
            "username": "testuser",
            "name": "test",
            "age": "20",
            "gender": "M",
            "password": "newpassword123",
            "cc": "2",
            "phone": "222",
            "email": "newuser@example.com"
        }
        response = self.client.post(self.register_url, data2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("username", response.data)  # duplicate error
    
    def test_register_invalid_email(self):
        """Test of registration with an invalid email address."""
        data = {
            "username": "testuser",
            "password": "password123",
            "email": "invalid-email"
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)  # hope that the mail is not valid

class LogoutViewTests(APITestCase):

    def setUp(self):
        # Create user for tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = '/api/logout/'  

    def test_logout_success(self):
        # Send POST request with correct credentials
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'testpassword'})
        
        # Verify that the logout was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Successful logout.'})

    def test_logout_invalid_credentials(self):
        # Send POST request with incorrect credentials
        response = self.client.post(self.url, {'username': 'testuser', 'password': 'wrongpassword'})
        
        # Verify that the authentication failed and a 401 error is returned.
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {'error': 'Invalid credentials.'})

    def test_logout_missing_credentials(self):
        # Send POST request without credentials
        response = self.client.post(self.url, {})
        
        # Verify that the username or password is missing and an error 400 is returned.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'Username and password are required.'})


