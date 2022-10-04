from django.core.management.base import BaseCommand
import csv
import ast
from ...models import City,Class,Country,State,Team,Twitter,Player,Position,Offer,HighSchool,Interest


class Command(BaseCommand):
    """Command class to handle function for inserting data into the database for players"""
    help = 'import data'

    def handle(self, *args, **options):
        """function for inserting player's data into table"""
        try:
            file = "/home/sonalis/web_scraping/player_management/player/player_data.csv"
            with open(file, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for word in reader:
                    # Inserting data of Country Model
                    try:
                        Country.objects.get_or_create(name=word[-1])
                    except Exception:
                        pass
                    # Inserting data of State Model
                    try:
                        city_state = str(word[6])
                        city_state_data = city_state.split(",")
                        State.objects.get_or_create(name=city_state_data[-1],country_id=Country.objects.filter(name=word[13]).first())
                    except ():
                        pass
                    # Inserting data of City Model
                    City.objects.get_or_create(city=city_state_data[0],
                                               state_id=State.objects.filter(name=city_state_data[-1]).first())
                    # Inserting data of Twitter Model
                    try:
                        Twitter.objects.get_or_create(profile_name=word[11])
                    except Exception:
                        pass
                    # Inserting data of Team Model
                    try:
                        team_data = word[12]
                        team_result = ast.literal_eval(team_data)
                        team = []
                        logo = []
                        for team_name in team_result:
                            team.append(team_name)
                            logo.append(team_result[team_name])
                            for value in range(len(team)):
                                team_exist = Team.objects.filter(name=team[value]).exists()
                                if False == team_exist:
                                    Team.objects.get_or_create(name=team[value], logo=logo[value])
                    except Exception:
                        pass

                    # Inserting data of Interest Model
                    interest_data = word[9]
                    interest_result = ast.literal_eval(interest_data)
                    commit = []
                    commit_team = []
                    try:
                        for commit_status in interest_result:
                            commit.append(commit_status)
                            commit_team.append(interest_result[commit_status])
                            for val in range(len(commit)):
                                team = Team.objects.filter(name=commit_team[val]).first()
                                Interest.objects.get_or_create(commited=commit[val], team_id=team,
                                                               recruited_by=word[10])

                    except:
                        Interest.objects.get_or_create(commited=word[9], recruited_by=word[10])

                    # Inserting data of High_school Model
                    try:
                        HighSchool.objects.get_or_create(high_school=word[5])
                    except Exception:
                        pass
                    # Inserting data of Offer Model
                    try:
                        offer_data = word[12]
                        offer_result = ast.literal_eval(offer_data)
                        offer = Offer.objects.create()
                        for i in offer_result:
                            team = Team.objects.get(name=i)
                            offer.teams.add(*[team.id])
                    except Exception:
                        pass

                    # Inserting data of Position Model
                    try:
                        Position.objects.get_or_create(position=word[2])
                    except Exception:
                        pass

                    # Inserting data of Class Model

                    Class.objects.get_or_create(class_year=word[7])

                    # Inserting data of Player Model

                    Player.objects.get_or_create(name=word[0],
                                                 image=word[1],
                                                 height=word[3],
                                                 weight=word[4],
                                                 country_id=Country.objects.filter(name=word[13]).first(),
                                                 class_id=Class.objects.filter(class_year=word[7]).first(),
                                                 position_id=Position.objects.filter(position=word[2]).first(),
                                                 city_id=City.objects.filter(city=city_state_data[0]).first(),
                                                 school_id=HighSchool.objects.filter(high_school=word[5]).first(),
                                                 commit_id=Interest.objects.filter(recruited_by=word[10]).first(),
                                                 offer_id=offer,
                                                 twitter_id=Twitter.objects.filter(profile_name=word[11]).first())
        except FileNotFoundError:
            pass



