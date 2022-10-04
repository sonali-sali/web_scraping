"""Importing Required modules"""
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import City,Class,Country,HighSchool,Interest,Team,Twitter,State,Position,Player,Offer


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""
    class Meta:
        """Assigning User as a model and their fields"""
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    """Register Serializer"""
    class Meta:
        """Setting fields values onto the User model"""
        model = User
        fields = ('id', 'username','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Override create method in serializer to hashing password field"""
        user = User(
            username=validated_data['username'],
            email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(AuthTokenSerializer):
    """Login serializer"""
    class Meta:
        """Setting fields values onto the User model"""
        model = User
        fields = ('id', 'username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}


class TeamSerializer(serializers.ModelSerializer):
    """Team serializer"""
    class Meta:
        """Setting fields values onto the Team model"""
        model = Team
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    """City Model serializer class"""
    class Meta:
        """Setting fields values onto the City model"""
        model = City
        fields = ('city', 'state_id')
        depth = 3


class StateSerializer(serializers.ModelSerializer):
    """State Model serializer class"""
    class Meta:
        """Setting fields values onto the State model"""
        model = State
        fields = ('name', 'country_id')
        depth = 1


class CountrySerializer(serializers.ModelSerializer):
    """Country Model serializer class"""
    class Meta:
        """Setting fields values onto the Country model"""
        model = Country
        fields = '__all__'


class HighschoolSerializer(serializers.ModelSerializer):
    """Highschool Model serializer class"""
    class Meta:
        """Setting fields values onto the Highschool model"""
        model = HighSchool
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    """Class  Model serializer class"""
    class Meta:
        """Setting fields values onto the Class model"""
        model = Class
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    """Offer  Model serializer class"""
    class Meta:
        """Setting fields values onto the Offer model"""
        model = Offer
        fields = '__all__'
        extra_kwargs = {
            'team_id': {
                'allow_empty': True
            }
        }
        depth =1


class PositionSerializer(serializers.ModelSerializer):
    """Position  Model serializer class"""
    class Meta:
        """Setting fields values onto the Position model"""
        model = Position
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):
    """Interest  Model serializer class"""
    class Meta:
        """Setting fields values onto the Interest model"""
        model = Interest
        fields = '__all__'
        depth =1


class TwitterSerializer(serializers.ModelSerializer):
    """Twiiter  Model serializer class"""
    class Meta:
        """Setting fields values onto the Twitter model"""
        model = Twitter
        fields = '__all__'
        depth = 1


class PlayerSerializer(serializers.ModelSerializer):
    """Player  Model serializer class"""
    class Meta:
        """Setting fields values onto the Player model"""
        model = Player
        fields = '__all__'
        depth = 1
