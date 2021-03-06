import itertools
import json
import requests
from selenium import webdriver


def get_players():
    players_urls = []
    players = json.loads(requests.get(url='http://127.0.0.1:8000/core/pitchers/?limit=400').text)['results']

    for player in players:
        players_urls.append(player['url'])
    return players_urls, players


driver = webdriver.Firefox()
players_scraped = 0
urls, players = get_players()
for player_url, player in zip(urls, players):
    try:
        driver.get(player_url.replace("stats", "game-log"))
        b_url = driver.find_element_by_xpath(
            '//div[contains(@id,"content")]//ul[contains(@class,"menu-player-page__batpitch")]/li[1]//div/a').get_attribute(
            "href")
        driver.get(b_url)
        s_url = driver.find_element_by_xpath(
            '//div[contains(@id,"content")]//ul[contains(@class,"menu-mega__game-log")]/li[7]/a').get_attribute("href")
        driver.get(s_url)

        date_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Date']")
        s = 0
        for date in date_list:
            if date.text == '':
                break
            s += 1

        team_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Team']")[1:s]
        opp_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Opp']")[1:s]
        bo_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BO']")[1:s]
        pos_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Pos']")[1:s]
        wpa_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='WPA']")[1:s]
        minus_wpa_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='-WPA']")[1:s]
        plus_wpa_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='+WPA']")[1:s]
        re24_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='RE24']")[1:s]
        rew_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='REW']")[1:s]
        pli_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='pLI']")[1:s]
        phli_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='phLI']")[1:s]
        wpa_li_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='WPA/LI']")[1:s]
        clutch_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Clutch']")[1:s]

        for date, team, opp, bo, pos, wpa, minus_wpa, plus_wpa, re24, rew, pli, phli, wpa_li, clutch in \
                itertools.zip_longest(date_list[1:s], team_list, opp_list, bo_list, pos_list, wpa_list, minus_wpa_list,
                                        plus_wpa_list, re24_list, rew_list, pli_list, phli_list, wpa_li_list, clutch_list):

            data = {
                'player': player['player'],
                'team_name': player['team'],
                'date': date.text,
                'team': team.text,
                'opp': opp.text,
                'bo': bo.text,
                'pos': pos.text,
                'wpa': wpa.text,
                'minus_wpa': minus_wpa.text,
                'plus_wpa': plus_wpa.text,
                're24': re24.text,
                'rew': rew.text,
                'pli': pli.text,
                'phli': phli.text,
                'wpa_li': wpa_li.text,
                'clutch': clutch.text
            }
            # print(data)
            headers = {'Content-type': 'application/json', 'Accept': '*/*'}
            requests.post(url='http://127.0.0.1:8000/core/dual-hitters-win-probability/', data=json.dumps(data), headers=headers)

        players_scraped += 1
        print(f'Player scraped : {players_scraped}')

    except KeyboardInterrupt:
        break

    except Exception as e:
        print(f'Player : {player["player"]} | Team : {player["team"]}')
        print(f"Error :{e}")

driver.quit()
