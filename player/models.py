"""importing models"""
from django.db import models


class Team(models.Model):
    """ Team Model"""
    name = models.CharField(max_length=30)
    logo = models.URLField(max_length=200,null=True)


class Country(models.Model):
    """ Country Model"""
    name = models.CharField(max_length=30)


class State(models.Model):
    """ State Model"""
    name = models.CharField(max_length=30)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)


class HighSchool(models.Model):
    """School Model"""
    high_school = models.CharField(max_length=100)


class City(models.Model):
    """ City model"""
    city = models.CharField(max_length=100)
    state_id = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)


class Class(models.Model):
    """Class model"""
    class_year = models.CharField(max_length=30)


class Offer(models.Model):
    """Offer model"""
    teams = models.ManyToManyField(Team, blank=True)


class Position(models.Model):
    """Position Model"""
    position = models.CharField(max_length=30)


class Interest(models.Model):
    """Interest model"""
    commited = models.CharField(max_length=100)
    team_id = models.ForeignKey(Team, on_delete=models.SET_NULL, null =True)
    recruited_by = models.CharField(max_length=100)


class Twitter(models.Model):
    """Twitter info model"""
    tweets_count = models.IntegerField(null=True)
    followers_count = models.IntegerField(null=True)
    following_count = models.IntegerField(null=True)
    last_tweet = models.CharField(max_length=500,null=True)
    retweets_count = models.IntegerField(null=True)
    profile_name = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)


class Player(models.Model):
    """Players Ranking Wise Model"""
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=100)
    height = models.CharField(max_length=100,null=True)
    weight = models.IntegerField(null=True)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    position_id = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    city_id = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    school_id = models.ForeignKey(HighSchool, on_delete=models.SET_NULL,null=True)
    commit_id = models.ForeignKey(Interest, on_delete=models.SET_NULL,null=True)
    offer_id = models.ForeignKey(Offer, on_delete=models.SET_NULL,null=True)
    twitter_id = models.ForeignKey(Twitter,on_delete=models.SET_NULL, null=True)
