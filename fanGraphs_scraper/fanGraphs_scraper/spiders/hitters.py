import json
import requests
import itertools
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


driver = webdriver.Chrome()


def get_players(role, t, d):
    try:
        if role == 'starting_lineup':
            slice = 9
            table = 1
            lineup_slice = 54
        else:
            slice = 4
            table = 2
            lineup_slice = 24

        pos_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "POS")]')[:slice]
        player_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "PLAYER")]')[:slice]
        url_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "PLAYER")]/a')[:slice]
        bats_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "BATS")]')[:slice]
        ovr_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[(@data-stat= "Ovr")]')[:slice]
        l_7_d_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "Last 7 Days")]')[:slice]
        lineups_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@class, "game-item")]')[:lineup_slice]
        lineups_list = np.array_split(lineups_list, slice)

        for pos, player, bats, ovr, l_7_d, lineups, url in itertools.zip_longest \
                    (pos_list, player_list, bats_list, ovr_list, l_7_d_list, lineups_list, url_list):
            if player.text != '':
                data = {
                    'role': role,
                    'team': t['name'],
                    'pos': pos.text,
                    'player': player.text,
                    'bats': bats.text,
                    'ovr': ovr.text,
                    'last_7_days': l_7_d.text,
                    'lineup1': lineups[0].text,
                    'lineup2': lineups[1].text,
                    'lineup3': lineups[2].text,
                    'lineup4': lineups[3].text,
                    'lineup5': lineups[4].text,
                    'lineup6': lineups[5].text,
                    'url': url.get_attribute("href")
                }

                headers = {'Content-type': 'application/json', 'Accept': '*/*'}
                requests.post(url='http://127.0.0.1:8000/core/hitter/', data=json.dumps(data), headers=headers)

    except Exception as e:
        print(f'Team : {team}')
        print(f"Error :{e}")

    except KeyboardInterrupt:
        driver.quit()


def get_teams():
    urls = []
    teams = json.loads(requests.get(url='http://127.0.0.1:8000/core/teams/').text)['results']

    for team_name in teams:
        if team_name['name'] == 'D-backs':
            team = 'diamondbacks'
        else:
            team = team_name['name']

        urls.append(
            f'https://www.fangraphs.com/roster-resource/depth-charts/{team.lower().replace(" ", "-")}')
    return urls, teams


url, team = get_teams()
scraped = 0

for team_url, team in zip(url, team):
    try:
        driver.get(team_url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(@class,"depth-charts__roster-tables")][1]//td[contains(@data-stat, "POS")]')))

        get_players(role='starting_lineup', t=team, d=driver)
        get_players(role='bench', t=team, d=driver)

        scraped += 1

    except KeyboardInterrupt:
        driver.quit()
    except Exception as e:
        print(f'Team : {team}')
        print(f"Error :{e}")

print(scraped)
driver.quit()
