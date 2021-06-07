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
            '//div[contains(@id,"content")]//ul[contains(@class,"menu-mega__game-log")]/li[10]/a').get_attribute("href")
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
        o_swing_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='O-Swing%']")[1:s]
        z_swing_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Z-Swing%']")[1:s]
        swing_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Swing%']")[1:s]
        o_contact_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='O-Contact%']")[1:s]
        z_contact_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Z-Contact%']")[1:s]
        contact_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Contact%']")[1:s]
        zone_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Zone%']")[1:s]
        f_strike_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='F-Strike%']")[1:s]
        swstr_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='SwStr%']")[1:s]

        for date, team, opp, bo, pos, o_swing_percentage, z_swing_percentage, swing_percentage, o_contact_percentage,\
                z_contact_percentage, contact_percentage, zone_percentage, f_strike_percentage, swstr_percentage\
                in itertools.zip_longest(date_list[1:s], team_list, opp_list, bo_list, pos_list,
                                         o_swing_percentage_list, z_swing_percentage_list, swing_percentage_list
                                         , o_contact_percentage_list, z_contact_percentage_list, contact_percentage_list
                                         , zone_percentage_list, f_strike_percentage_list, swstr_percentage_list):

            data = {
                'player': player['player'],
                'team_name': player['team'],
                'date': date.text,
                'team': team.text,
                'opp': opp.text,
                'bo': bo.text,
                'pos': pos.text,
                'o_swing_percent': o_swing_percentage.text,
                'z_swing_percentage': z_swing_percentage.text,
                'swing_percentage': swing_percentage.text,
                'o_contact_percentage': o_contact_percentage.text,
                'z_contact_percentage': z_contact_percentage.text,
                'contact_percentage': contact_percentage.text,
                'zone_percentage': zone_percentage.text,
                'f_strike_percentage': f_strike_percentage.text,
                'swstr_percentage': swstr_percentage.text
            }
            # print(data)
            headers = {'Content-type': 'application/json', 'Accept': '*/*'}
            requests.post(url='http://127.0.0.1:8000/core/dual-hitters-plate-discipline/', data=json.dumps(data), headers=headers)

        players_scraped += 1
        print(f'Player scraped : {players_scraped}')

    except KeyboardInterrupt:
        driver.quit()
        break

    except Exception as e:
        print(f'Player : {player["player"]} | Team : {player["team"]}')
        print(f"Error :{e}")

driver.quit()
