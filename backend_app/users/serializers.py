from rest_framework import serializers
from .models import User, UserProfile, Document
from django.contrib.auth import get_user_model

# Get the user model configured in Django (custom or default)
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # Django handles the hash
        )
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'age', 'gender', 'cc', 'phone', 'email']

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    cc = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("The user name is already registered.")
        return value

    def validate_email(self, value):
        if UserProfile.objects.filter(email=value).exists():
            raise serializers.ValidationError("The email name is already registered.")
        return value

    def create(self, validated_data):
        # Create user using Django Allauth or directly with DRF
        user_data = {
            'username': validated_data['username'],
            'password': validated_data['password'],
        }
        user = User.objects.create_user(**user_data)

        # Create associated user profile
        profile_data = {
            'user': user,
            'name': validated_data['name'],
            'age': validated_data['age'],
            'gender': validated_data['gender'],
            'cc': validated_data['cc'],
            'phone': validated_data['phone'],
            'email': validated_data['email'],
        }
        UserProfile.objects.create(**profile_data)
        return user

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'user', 'file', 'uploaded_at', 'updated_at']
