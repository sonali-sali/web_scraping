"""Importing required modules"""
import json
from django.core.management.base import BaseCommand
from ...models import Class, Interest, Position,Offer,HighSchool,City, State, Team, Player
from ...teamwise_scrap import get_teamwise_player_attributes
import ast
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



class Command(BaseCommand):
    """Command class to handle function for updating data of players"""
    help = 'import data'

    def handle(self, *args, **options):
        """function to update players attributes"""
        try:
            chromeoptions = webdriver.ChromeOptions()
            chromeoptions.add_argument('--window-size=1920,1080')
            chromeoptions.headless = True
            chromeoptions.add_argument('--no-sandbox')
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeoptions)
            driver.get("https://247sports.com/college/football/recruiting/")
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, "/html/body/div[1]/section/header/div/div/nav/ul/li[7]/button/b[2]").click()
            driver.find_element(By.XPATH, "/html/body/div[1]/section/header/div/div/nav/ul/li[7]/div/ul/li[1]/a").click()
            for player_id in range(1, 10):
                player_data = Player.objects.get(id=player_id)
                driver.find_element(By.XPATH,"/html/body/section[1]/section/div/section[2]/section/section/section/div/section[1]/form/input").send_keys(player_data.name)
                time.sleep(5)
                driver.find_element(By.XPATH,"/html/body/section[1]/section/div/section[2]/section/section/section/div/section[1]/form/button").click()
                time.sleep(5)
                driver.find_element(By.XPATH,"/html/body/section[1]/section/div/section[2]/section/section/section/div/div[1]/ul[2]/li/ul/li[2]/a").click()
                player = get_teamwise_player_attributes(driver)
                values = []
                for player_datas in player:
                    values.append(player[player_datas])
                print(values[0])
                try:
                    if values[0] == player_data.name:
                        print(player_data.name)
                    else:
                        Player.objects.filter(id=player_id).update(name=values[0])
                except NoSuchElementException:
                    pass
                try:
                    if values[1] == player_data.image:
                        print(player_data.image)
                    else:
                        Player.objects.filter(id=player_id).update(image=values[1])
                except NoSuchElementException:
                    pass
                """Updating Player Position"""
                try:
                    Position.objects.update_or_create(position=values[2])
                except NoSuchElementException:
                    pass

                """Updating Player Height"""
                try:
                    if values[3] == player_data.height:
                        print(player_data.height)
                    else:
                        Player.objects.filter(id=player_id).update(height=values[3])
                except NoSuchElementException:
                    pass

                """Updating Player weight"""
                try:
                    if values[4] == player_data.weight:
                        print(player_data.weight)
                    else:
                        Player.objects.filter(id=player_id).update(weight=values[4])
                        print("Weight updated successfully")
                except NoSuchElementException:
                    pass

                """Updating Player Highschool"""
                try:
                    HighSchool.objects.update_or_create(high_school=values[5])
                    print("Highschool updated successfully")

                except NoSuchElementException:
                    pass

                """Updating Player City"""
                try:
                    city = values[6].split(",")
                    City.objects.update_or_create(city=city[0])
                    print("City updated successfully")
                except NoSuchElementException:
                    pass

                """Updating Player State"""
                try:
                    city = values[6].split(",")
                    State.objects.update_or_create(name=city[-1])
                    print("City updated successfully")
                except NoSuchElementException:
                    pass

                """Updating Player Class year"""
                try:
                    Class.objects.update_or_create(class_year=values[7])
                except NoSuchElementException:
                    pass

                """Updating Player Interest"""
                commit = json.dumps(values[9])
                try:
                    res = ast.literal_eval(commit)
                    commit_status = []
                    commit_team = []
                    for data in res:
                        commit_status.append(data)
                        commit_team.append(res[data])
                        team = Team.objects.filter(name=commit_team[0]).first()
                        Interest.objects.filter(id=player_id).update(commited=commit_status[0], team_id=team,recruited_by=values[10])
                except NoSuchElementException:
                    Interest.objects.filter(id=player_id).update(commited=values[9], recruited_by=values[10])

                """Update Player offer"""
                try:
                    offer_data = json.dumps(values[12])
                    res = ast.literal_eval(offer_data)
                    offer_id = Offer.objects.get(id=player_id)
                    team_id = []
                    for team_name in res:
                        team = Team.objects.get(name=team_name)
                        team_id.append(team.pk)
                    offer_id.teams.set(team_id, clear=True)

                except NoSuchElementException:
                    pass

                driver.get("https://247sports.com/Season/2023-Football/Recruits/")
        except NoSuchElementException:
            pass

