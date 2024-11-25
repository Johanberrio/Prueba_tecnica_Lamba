from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from backend import settings

# Extending the default User model
class User(AbstractUser):
    # Overriding the username field to ensure it's unique
    username = models.CharField(max_length=150, unique=True)
    # Defining a password field for storing hashed passwords
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
# Defining a profile model that extends user-related information
class UserProfile(models.Model):
    # One-to-one relationship with the User model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Storing additional information about the user
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    cc = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Model for storing uploaded documents
class Document(models.Model):
    file = models.FileField(upload_to='documents/')  # Path where documents are stored
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Document {self.id} - {self.uploaded_at}"
