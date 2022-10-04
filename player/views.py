from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer,LoginSerializer,TwitterSerializer,TeamSerializer,InterestSerializer,RegisterSerializer,CountrySerializer,ClassSerializer,CitySerializer,HighschoolSerializer,PlayerSerializer,PositionSerializer,StateSerializer,OfferSerializer
from django.contrib.auth import login
from .models import Team,State,City,Interest,Player,Position,Class,Country,HighSchool,Offer,Twitter
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User


class RegisterAPI(generics.GenericAPIView):
    """Register API"""
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]})


class LoginAPI(generics.GenericAPIView):
    """User Login API"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)
        return Response({
            'user_id': user.pk,
            "token": AuthToken.objects.create(user)[1],})


class UserListCreate(generics.ListCreateAPIView):
    """User List and create API"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Team retrieve, update and delete API"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamList(generics.ListCreateAPIView):
    """Team List and create API"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    """Team retrieve, update and delete API"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CityList(generics.ListCreateAPIView):
    """City List and create API"""
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    """State retrieve, update and delete API"""
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StateList(generics.ListCreateAPIView):
    """State List and create API"""
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    """Country retrieve, update and delete API"""
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CountryList(generics.ListCreateAPIView):
    """Country List and create API"""
    queryset = State.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    """City retrieve, update and delete API"""
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class HighschoolList(generics.ListCreateAPIView):
    """Highschool List and create API"""
    queryset = HighSchool.objects.all()
    serializer_class = HighschoolSerializer


class HighschoolDetail(generics.RetrieveUpdateDestroyAPIView):
    """Highschool retrieve, update and delete API"""
    queryset = HighSchool.objects.all()
    serializer_class = HighschoolSerializer


class ClassList(generics.ListCreateAPIView):
    """Class List and create API"""
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassDetail(generics.RetrieveUpdateDestroyAPIView):
    """Class retrieve, update and delete API"""
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class OfferList(generics.ListCreateAPIView):
    """Offer List and create API"""
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferDetail(generics.RetrieveUpdateDestroyAPIView):
    """Offer retrieve, update and delete API"""
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class PositionList(generics.ListCreateAPIView):
    """Position List and create API"""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionDetail(generics.RetrieveUpdateDestroyAPIView):
    """Position retrieve, update and delete API"""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class InterestList(generics.ListCreateAPIView):
    """Interest List and create API"""
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class InterestDetail(generics.RetrieveUpdateDestroyAPIView):
    """Interest retrieve, update and delete API"""
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class TwitterList(generics.ListCreateAPIView):
    """Twitter List and create API"""
    queryset = Twitter.objects.all()
    serializer_class = TwitterSerializer


class TwitterDetail(generics.RetrieveUpdateDestroyAPIView):
    """Twitter retrieve, update and delete API"""
    queryset = Twitter.objects.all()
    serializer_class = TwitterSerializer


class PlayerList(generics.ListCreateAPIView):
    """Player List and create API"""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    """Player retrieve, update and delete API"""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
