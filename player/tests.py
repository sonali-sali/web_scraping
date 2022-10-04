"""Importing required modules"""
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from .models import City,Class,Country,State,HighSchool,Interest,Player,Position,Offer,Team,Twitter

User = get_user_model()


class TestSetUp(APITestCase):
    """Parent Class"""
    def setUp(self):
        """SetUp function to set the data for using in child class"""
        self.data = User.objects.create_user(id=1, username="aru",email="aru@gmail.com",
                                             password="aru@123")
        self.country = Country.objects.create(id=1,name='USA')
        self.state = State.objects.create(id=1,name='CA',country_id=self.country)
        self.city = City.objects.create(id=1,city='Norwalk',state_id=self.state)
        self.highschool = HighSchool.objects.create(id=1,high_school='Cerritos College')
        self.team = Team.objects.create(id=1,name='albam',logo='https://s3media.247sports.com/Uploads/Assets/183/613/10613183.jpg?fit=crop&width=100&fit=crop')
        self.classs = Class.objects.create(id=1,class_year='2023')
        self.offer = Offer.objects.create()
        team=Team.objects.get(name='albam')
        self.offer.teams.add(team.id)
        self.position = Position.objects.create(id=1,position='edge')
        self.interest = Interest.objects.create(id=1,commited='commited',
                                                team_id=self.team,recruited_by='kk,jj')
        self.twitter = Twitter.objects.create(id=1,tweets_count=45,followers_count=55,
                                              following_count=44,last_tweet='frferrfef',
                                              retweets_count=44,profile_name='@soni',location='uk')
        self.player = Player.objects.create(id=1,name='soni',image=
        'https://s3media.247sports.com/Uploads/Assets/176/746/10746176.jpg?fit=crop&width=100&fit=crop',
                                            height='6-2',weight=230,country_id=self.country,
                                            class_id=self.classs,
                                            position_id=self.position,city_id=self.city,
                                            school_id=self.highschool,commit_id=self.interest,
                                            offer_id=self.offer,twitter_id=self.twitter)
        self.data = {'id':2,'name':'hari','image':'https://s3media.247sports.com/Uploads/Player/0/0.jpg?fit=crop&width=100&fit=crop',
                                            'height':'6-2','weight':230,'country_id':self.country.pk,
                                            'class_id':self.classs.pk,
                                            'position_id':self.position.pk,'city_id':self.city.pk,
                                            'school_id':self.highschool.pk,'commit_id':self.interest.pk,'offer_id':self.offer.pk,'twitter_id':self.twitter.pk}


class UserLogin(TestSetUp):
    """User Login TestCase"""
    def test_user_login(self):
        """defining function to check testcases for Login"""
        login_url = reverse('login')
        self.client.force_authenticate(user=self.data)
        data = {"username": "aru", "password": "aru@123"}
        response = self.client.post(login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PlayerTestcase(TestSetUp):
    """TestCases for Player Model"""

    def test_user_create_playerdata(self):
        """defining function to check testcases for create Player data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        player_url = reverse('player')
        response = self.client.post(player_url,self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_playerdata(self):
        """defining function to check testcases for get Player data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('player'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_get_playerdata(self):
        """defining function to check testcases for get Player data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        player = Player.objects.get(id=1)
        response = self.client.get(reverse('playerdetail', args=[player.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_playerdata(self):
        """defining function to check testcases for update Player data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        player = Player.objects.get(id=1)
        response = self.client.patch(reverse('playerdetail', args=[player.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_playerdata(self):
        """defining function to check testcases for delete Player data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        player = Player.objects.get(id=1)
        response = self.client.delete(reverse('playerdetail', args=[player.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymoususer_read_playerdata(self):
        """defining function to check testcases for read Player data for anonymous user"""
        response = self.client.get(reverse('player'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_create_playerdata(self):
        """defining function to check testcases for read Player data for anonymous user"""
        response = self.client.get(reverse('player'),self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_get_playerdata(self):
        """defining function to check testcases for delete Player data for anonymous user"""
        player = Player.objects.get(id=1)
        response = self.client.get(reverse('playerdetail', args=[player.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymoususer_update_playerdata(self):
        """defining function to check testcases for update Player data for anonymous user"""
        player = Player.objects.get(id=1)
        response = self.client.patch(reverse('playerdetail', args=[player.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymoususer_delete_playerdata(self):
        """defining function to check testcases for delete Player data for anonymous user"""
        player = Player.objects.get(id=1)
        response = self.client.delete(reverse('playerdetail', args=[player.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class CountryTestcase(TestSetUp):
    """TestCases for Country Model"""

    def test_user_create_countrydata(self):
        """defining function to check testcases for create country data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        country_url = reverse('country')
        data = {'name':'USA'}
        response = self.client.post(country_url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_countrydata(self):
        """defining function to check testcases for read country data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        country_url = reverse('country')
        response = self.client.get(country_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_get_country(self):
        """defining function to check testcases for get Country data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        country = Country.objects.get(id=1)
        response = self.client.get(reverse('countrydetail', args=[country.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_country(self):
        """defining function to check testcases for update Country data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        country = Country.objects.get(id=1)
        response = self.client.patch(reverse('countrydetail', args=[country.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_country(self):
        """defining function to check testcases for delete Country data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        country = Country.objects.get(id=1)
        response = self.client.delete(reverse('countrydetail', args=[country.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_countrydata(self):
        """defining function to check testcases for create country data for unauthenticated user"""
        country_url = reverse('country')
        data = {'name': 'USA'}
        response = self.client.post(country_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_countrydata(self):
        """defining function to check testcases for read country data for unauthenticated user"""
        country_url = reverse('country')
        response = self.client.get(country_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_get_country(self):
        """defining function to check testcases for get Country data for unauthenticated user"""
        country = Country.objects.get(id=1)
        response = self.client.get(reverse('countrydetail', args=[country.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_country(self):
        """defining function to check testcases for update Country data for unauthenticated user"""
        country = Country.objects.get(id=1)
        response = self.client.patch(reverse('countrydetail', args=[country.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_country(self):
        """defining function to check testcases for delete Country data for unauthenticated user"""
        country = Country.objects.get(id=1)
        response = self.client.delete(reverse('countrydetail', args=[country.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TeamTestcase(TestSetUp):
    """TestCases for Team Model"""


    def test_user_create_teamdata(self):
        """defining function to check testcases for create team data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        team_url = reverse('team')
        response = self.client.post(team_url, {'name': 'kllbam','logo':"https://s3media.247sports.com/Uploads/Player/0/0.jpg?fit=crop&width=100&fit=crop"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_team(self):
        """defining function to check testcases for read Team data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('team'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_get_team(self):
        """defining function to check testcases for get Team data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        team = Team.objects.get(id=1)
        response = self.client.get(reverse('teamdetail', args=[team.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_team(self):
        """defining function to check testcases for update Team data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        team = Team.objects.get(id=1)
        response = self.client.patch(reverse('teamdetail', args=[team.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_team(self):
        """defining function to check testcases for delete Team data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        team = Team.objects.get(id=1)
        response = self.client.delete(reverse('teamdetail', args=[team.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_team(self):
        """defining function to check testcases for create Team data for unauthenticated user"""
        data = { 'name':'avi','logo':'https://s3media.247sports.com/Uploads/Player/0/0.jpg?fit=crop&width=100&fit=crop'}
        response = self.client.post(reverse('team'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_team(self):
        """defining function to check testcases for read Team data for unauthenticated user"""
        response = self.client.get(reverse('team'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_get_team(self):
        """defining function to check testcases for get Team data for unauthenticated user"""
        team = Team.objects.get(id=1)
        response = self.client.get(reverse('teamdetail', args=[team.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_team(self):
        """defining function to check testcases for update Team data for unauthenticated user"""
        team = Team.objects.get(id=1)
        response = self.client.patch(reverse('teamdetail', args=[team.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_team(self):
        """defining function to check testcases for delete Team data for unauthenticated user"""
        team = Team.objects.get(id=1)
        response = self.client.delete(reverse('teamdetail', args=[team.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class HighSchoolTestcase(TestSetUp):
    """TestCases for HighSchool Model"""

    def test_user_create_highschool(self):
        """defining function to check testcases for create HighSchool data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        data = {'high_school':'Highland'}
        response = self.client.post(reverse('highschool'),data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_highschool(self):
        """defining function to check testcases for read HighSchool data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('highschool'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_user_get_highschool(self):
        """defining function to check testcases for read HighSchool data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        highschool = HighSchool.objects.get(id=1)
        response = self.client.get(reverse('highschooldetail', args=[highschool.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_highschool(self):
        """defining function to check testcases for update HighSchool data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        highschool = HighSchool.objects.get(id=1)
        response = self.client.patch(reverse('highschooldetail', args=[highschool.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_highschool(self):
        """defining function to check testcases for delete HighSchool data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        highschool = HighSchool.objects.get(id=1)
        response = self.client.delete(reverse('highschooldetail', args=[highschool.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_highschool(self):
        """defining function to check testcases for create HighSchool data for unauthenticated user"""
        data = {'high_school': 'Highland'}
        response = self.client.post(reverse('highschool'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_highschool(self):
        """defining function to check testcases for read HighSchool data for unauthenticated user"""
        response = self.client.get(reverse('highschool'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_get_highschool(self):
        """defining function to check testcases for get HighSchool data for unauthenticated user"""
        highschool = HighSchool.objects.get(id=1)
        response = self.client.get(reverse('highschooldetail', args=[highschool.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_highschool(self):
        """defining function to check testcases for update HighSchool data for unauthenticated user"""
        highschool = HighSchool.objects.get(id=1)
        response = self.client.patch(reverse('highschooldetail', args=[highschool.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_highschool(self):
        """defining function to check testcases for delete HighSchool data for unauthenticated user"""
        highschool = HighSchool.objects.get(id=1)
        response = self.client.delete(reverse('highschooldetail', args=[highschool.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ClassTestcase(TestSetUp):
    """TestCases for Class Model"""

    def test_user_create_class(self):
        """defining function to check testcases for create Class data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        data = {'class_year':'2022'}
        response = self.client.post(reverse('class'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_class(self):
        """defining function to check testcases for read Class data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('class'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_user_get_class(self):
        """defining function to check testcases for get Class data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        classs = Class.objects.get(id=1)
        response = self.client.get(reverse('classdetail', args=[classs.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_class(self):
        """defining function to check testcases for update Class data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        classs = Class.objects.get(id=1)
        response = self.client.patch(reverse('classdetail', args=[classs.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_class(self):
        """defining function to check testcases for update Class data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        classs = Class.objects.get(id=1)
        response = self.client.delete(reverse('classdetail', args=[classs.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_class(self):
        """defining function to check testcases for create Class data for unauthenticated user"""
        data = {'class_year':'2022'}
        response = self.client.post(reverse('class'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_class(self):
        """defining function to check testcases for read Class data for unauthenticated user"""
        response = self.client.get(reverse('class'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    def test_anonymous_user_get_class(self):
        """defining function to check testcases for get Class data for unauthenticated user"""
        classs = Class.objects.get(id=1)
        response = self.client.get(reverse('classdetail', args=[classs.pk]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_class(self):
        """defining function to check testcases for update Class data for unauthenticated user"""
        classs = Class.objects.get(id=1)
        response = self.client.patch(reverse('classdetail', args=[classs.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_class(self):
        """defining function to check testcases for update Class data for unauthenticated user"""
        classs = Class.objects.get(id=1)
        response = self.client.delete(reverse('classdetail', args=[classs.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



class CityTestcase(TestSetUp):
    """TestCases for City Model"""

    def test_user_create_city(self):
        """defining function to check testcases for create City data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        data = {'city':'sssa','state_id':self.state.pk}
        response = self.client.post(reverse('city'),data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_city(self):
        """defining function to check testcases for read City data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('city'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_user_get_city(self):
        """defining function to check testcases for get City data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        city = City.objects.get(id=1)
        response = self.client.get(reverse('citydetail', args=[city.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_city(self):
        """defining function to check testcases for update City data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        city = City.objects.get(id=1)
        response = self.client.patch(reverse('citydetail', args=[city.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_city(self):
        """defining function to check testcases for delete City data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        city = City.objects.get(id=1)
        response = self.client.delete(reverse('citydetail', args=[city.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_city(self):
        """defining function to check testcases for create City data for unauthenticated user"""
        data = {'city': 'sssa', 'state_id': self.state.pk}
        response = self.client.post(reverse('city'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_city(self):
        """defining function to check testcases for read City data for unauthenticated user"""
        response = self.client.get(reverse('city'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_get_city(self):
        """defining function to check testcases for get City data for unauthenticated user"""
        city = City.objects.get(id=1)
        response = self.client.get(reverse('citydetail', args=[city.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_city(self):
        """defining function to check testcases for update City data for unauthenticated user"""
        city = City.objects.get(id=1)
        response = self.client.patch(reverse('citydetail', args=[city.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_city(self):
        """defining function to check testcases for delete City data for unauthenticated user"""
        city = City.objects.get(id=1)
        response = self.client.delete(reverse('citydetail', args=[city.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)




class StateTestcase(TestSetUp):
    """TestCases for State Model"""

    def test_user_create_state(self):
        """defining function to check testcases for create State data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        data={'name':'xys','country_id':self.country.pk}
        response = self.client.post(reverse('state'),data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_state(self):
        """defining function to check testcases for read State data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('state'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_user_get_state(self):
        """defining function to check testcases for get State data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        state = State.objects.get(id=1)
        response = self.client.get(reverse('statedetail', args=[state.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_state(self):
        """defining function to check testcases for update State data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        state = State.objects.get(id=1)
        response = self.client.patch(reverse('statedetail', args=[state.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_state(self):
        """defining function to check testcases for delete State data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        state = State.objects.get(id=1)
        response = self.client.delete(reverse('statedetail', args=[state.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_state(self):
        """defining function to check testcases for create State data for unauthenticated user"""
        data={'name':'xys'}
        response = self.client.post(reverse('state'),data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_state(self):
        """defining function to check testcases for read State data for unauthenticated user"""
        response = self.client.get(reverse('state'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    def test_anonymous_user_get_state(self):
        """defining function to check testcases for get State data for unauthenticated user"""
        state = State.objects.get(id=1)
        response = self.client.get(reverse('statedetail', args=[state.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_state(self):
        """defining function to check testcases for update State data for unauthenticated user"""
        state = State.objects.get(id=1)
        response = self.client.patch(reverse('statedetail', args=[state.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_state(self):
        """defining function to check testcases for delete State data for unauthenticated user"""
        state = State.objects.get(id=1)
        response = self.client.delete(reverse('statedetail', args=[state.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)




class PositionTestcase(TestSetUp):
    """TestCases for Position Model"""

    def test_user_create_position(self):
        """defining function to check testcases for create Position data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        data={'position':'Edge'}
        response = self.client.post(reverse('position'),data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_position(self):
        """defining function to check testcases for read Position data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('position'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_user_get_position(self):
        """defining function to check testcases for get Position data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        position = Position.objects.get(id=1)
        response = self.client.get(reverse('positiondetail', args=[position.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_position(self):
        """defining function to check testcases for update Position data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        position = Position.objects.get(id=1)
        response = self.client.patch(reverse('positiondetail', args=[position.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_position(self):
        """defining function to check testcases for delete Position data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        position = Position.objects.get(id=1)
        response = self.client.delete(reverse('positiondetail', args=[position.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_position(self):
        """defining function to check testcases for create Position data for unauthenticated user"""
        data={'position':'Edge'}
        response = self.client.post(reverse('position'),data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_position(self):
        """defining function to check testcases for read Position data for unauthenticated user"""
        response = self.client.get(reverse('position'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    def test_anonymous_user_get_position(self):
        """defining function to check testcases for get Position data for unauthenticated user"""
        position = Position.objects.get(id=1)
        response = self.client.get(reverse('positiondetail', args=[position.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_position(self):
        """defining function to check testcases for update Position data for unauthenticated user"""
        position = Position.objects.get(id=1)
        response = self.client.patch(reverse('positiondetail', args=[position.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_position(self):
        """defining function to check testcases for delete Position data for unauthenticated user"""
        position = Position.objects.get(id=1)
        response = self.client.delete(reverse('positiondetail', args=[position.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class InterestTestcase(TestSetUp):
    """TestCases for Interest Model"""

    def test_user_create_interest(self):
        """defining function to check testcases for create Interest data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        data={'commited':'Enrolled','team_id':self.team.pk,'recruited_by':"['Johnny Nansen']"}
        response = self.client.post(reverse('interest'),data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_interest(self):
        """defining function to check testcases for read Interest data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('interest'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_user_get_interest(self):
        """defining function to check testcases for get Interest data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        interest = Interest.objects.get(id=1)
        response = self.client.get(reverse('interestdetail', args=[interest.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_interest(self):
        """defining function to check testcases for update Interest data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        interest = Interest.objects.get(id=1)
        response = self.client.patch(reverse('interestdetail', args=[interest.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_interest(self):
        """defining function to check testcases for delete Interest data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        interest = Interest.objects.get(id=1)
        response = self.client.delete(reverse('interestdetail', args=[interest.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_interest(self):
        """defining function to check testcases for create Interest data for unauthenticated user"""
        data = {'commited': 'Enrolled', 'team_id': self.team.pk, 'recruited_by': "['Johnny Nansen']"}
        response = self.client.post(reverse('interest'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_interest(self):
        """defining function to check testcases for read Interest data for unauthenticated user"""
        response = self.client.get(reverse('interest'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_get_interest(self):
        """defining function to check testcases for get Interest data for unauthenticated user"""
        interest = Interest.objects.get(id=1)
        response = self.client.get(reverse('interestdetail', args=[interest.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_interest(self):
        """defining function to check testcases for update Interest data for unauthenticated user"""
        interest = Interest.objects.get(id=1)
        response = self.client.patch(reverse('interestdetail', args=[interest.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_interest(self):
        """defining function to check testcases for delete Interest data for unauthenticated user"""
        interest = Interest.objects.get(id=1)
        response = self.client.delete(reverse('interestdetail', args=[interest.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class OfferTestcase(TestSetUp):
    """TestCases for Offer Model"""

    def test_user_read_offer(self):
        """defining function to check testcases for create Offer data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('offer'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_user_get_offer(self):
        """defining function to check testcases for get Offer data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        offer = Offer.objects.get(teams=1)
        response = self.client.get(reverse('offerdetail', args=[offer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_offer(self):
        """defining function to check testcases for update Offer data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        offer = Offer.objects.get(teams=1)
        response = self.client.patch(reverse('offerdetail', args=[offer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_offer(self):
        """defining function to check testcases for delete Offer data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        offer = Offer.objects.get(teams=1)
        response = self.client.delete(reverse('offerdetail', args=[offer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_offer(self):
        """defining function to check testcases for create Offer data for unauthenticated user"""
        data = {'team_id': self.team.pk}
        response = self.client.post(reverse('offer'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_offer(self):
        """defining function to check testcases for create Offer data for unauthenticated user"""
        response = self.client.get(reverse('offer'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_get_offer(self):
        """defining function to check testcases for get Offer data for unauthenticated user"""
        offer = Offer.objects.get(teams=1)
        response = self.client.get(reverse('offerdetail', args=[offer.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_offer(self):
        """defining function to check testcases for update Offer data for unauthenticated user"""
        offer = Offer.objects.get(teams=1)
        response = self.client.patch(reverse('offerdetail', args=[offer.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_offer(self):
        """defining function to check testcases for delete Offer data for unauthenticated user"""
        offer = Offer.objects.get(teams=1)
        response = self.client.delete(reverse('offerdetail', args=[offer.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TwitterTestcase(TestSetUp):
    """TestCases for Twitter Model"""

    def test_user_create_twitter(self):
        """defining function to check testcases for create Twitter data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        data={'id': 1, 'tweets_count': 45, 'followers_count':55,
        'following_count':44, 'last_tweet':'frferrfef',
        'retweets_count':44, 'profile_name':'@sona', 'location':'uk'}
        response = self.client.post(reverse('twitter'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_read_twitter(self):
        """defining function to check testcases for read Twitter data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('twitter'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_get_twitter(self):
        """defining function to check testcases for get Twitter data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        twitter = Twitter.objects.get(id=1)
        response = self.client.get(reverse('twitterdetail', args=[twitter.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_twitter(self):
        """defining function to check testcases for update Twitter data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        twitter = Twitter.objects.get(id=1)
        response = self.client.patch(reverse('twitterdetail', args=[twitter.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete_twitter(self):
        """defining function to check testcases for delete Twitter data for authenticated user"""
        user = User.objects.get(username='aru')
        self.client.force_authenticate(user=user)
        twitter = Twitter.objects.get(id=1)
        response = self.client.delete(reverse('twitterdetail', args=[twitter.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_anonymous_user_create_twitter(self):
        """defining function to check testcases for create Twitter data for unauthenticated user"""
        data = {'id': 1, 'tweets_count': 45, 'followers_count': 55,
                'following_count': 44, 'last_tweet': 'frferrfef',
                'retweets_count': 44, 'profile_name': '@sonali', 'location': 'uk'}
        response = self.client.post(reverse('twitter'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_read_twitter(self):
        """defining function to check testcases for read Twitter data for unauthenticated user"""
        response = self.client.get(reverse('twitter'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_get_twitter(self):
        """defining function to check testcases for get Twitter data for unauthenticated user"""
        twitter = Twitter.objects.get(id=1)
        response = self.client.get(reverse('twitterdetail', args=[twitter.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_update_twitter(self):
        """defining function to check testcases for update Twitter data for unauthenticated user"""
        twitter = Twitter.objects.get(id=1)
        response = self.client.patch(reverse('twitterdetail', args=[twitter.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_anonymous_user_delete_twitter(self):
        """defining function to check testcases for delete Twitter data for unauthenticated user"""
        twitter = Twitter.objects.get(id=1)
        response = self.client.delete(reverse('twitterdetail', args=[twitter.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
