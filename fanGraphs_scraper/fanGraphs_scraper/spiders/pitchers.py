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
        if role == 'starting_rotation':
            slice = 5
            table = 3
            lastdays_slice = 30
            lastdays_list = d.find_elements_by_xpath(
                f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@class, "game-item")]')[
                            :lastdays_slice]
        else:
            slice = 9
            table = 4
            lastdays_slice = 54
            lastdays_list = d.find_elements_by_xpath(
                f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "specialBullpenUsage")]')[
                            :lastdays_slice]

        pos_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "POS")]')[:slice]
        player_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "PLAYER")]')[:slice]
        url_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "PLAYER")]/a')[:slice]
        thr_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "THR")]')[:slice]
        ovr_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[(@data-stat= "Ovr")]')[:slice]
        l_14_d_list = d.find_elements_by_xpath(
            f'//div[contains(@class,"depth-charts__roster-tables")][{table}]//td[contains(@data-stat, "Last 14 Days")]')[:slice]
        lastdays_list = np.array_split(lastdays_list, slice)

        print(f'Team : {t["name"]}')
        for pos, player, thr, ovr, l_14_d, lastdays, url in itertools.zip_longest \
                    (pos_list, player_list, thr_list, ovr_list, l_14_d_list, lastdays_list, url_list):
            if player.text != '':
                data = {
                    'role': role,
                    'team': t['name'],
                    'pos': pos.text,
                    'player': player.text,
                    'thr': thr.text,
                    'ovr': ovr.text,
                    'last_14_days': l_14_d.text,
                    'day1': lastdays[0].text,
                    'day2': lastdays[1].text,
                    'day3': lastdays[2].text,
                    'day4': lastdays[3].text,
                    'day5': lastdays[4].text,
                    'day6': lastdays[5].text,
                    'url': url.get_attribute("href")
                }

                headers = {'Content-type': 'application/json', 'Accept': '*/*'}
                requests.post(url='http://127.0.0.1:8000/core/pitcher/', data=json.dumps(data), headers=headers)

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
# url = ['https://www.fangraphs.com/roster-resource/depth-charts/white-sox']
# team = [{'name': 'White Sox'}]
for team_url, team in zip(url, team):
    try:
        driver.get(team_url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[contains(@class,"depth-charts__roster-tables")][1]//td[contains(@data-stat, "POS")]')))

        get_players(role='starting_rotation', t=team, d=driver)
        get_players(role='bullpen', t=team, d=driver)

        scraped += 1

    except KeyboardInterrupt:
        driver.quit()
    except Exception as e:
        print(f'Team : {team}')
        print(f"Error :{e}")

print(scraped)
driver.quit()
