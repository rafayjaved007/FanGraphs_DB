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
            '//div[contains(@id,"content")]//ul[contains(@class,"menu-mega__game-log")]/li[3]/a').get_attribute("href")
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
        bb_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BB%']")[1:s]
        k_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='K%']")[1:s]
        bb_k_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BB/K']")[1:s]
        avg_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='AVG']")[1:s]
        obp_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='OBP']")[1:s]
        slg_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='SLG']")[1:s]
        ops_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='OPS']")[1:s]
        iso_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='ISO']")[1:s]
        spd_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='Spd']")[1:s]
        babip_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BABIP']")[1:s]
        wrc_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='wRC']")[1:s]
        wraa_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='wRAA']")[1:s]
        woba_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='wOBA']")[1:s]
        wrc_plus_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='wRC+']")[1:s]

        for date, team, opp, bo, pos, bb_percentage, k_percentage, bb_k, avg, obp, slg, ops, iso, spd, babip, wrc,\
            wraa, woba, wrc_plus in itertools.zip_longest(date_list[1:s], team_list, opp_list, bo_list, pos_list,
                                                 bb_percentage_list, k_percentage_list, bb_k_list, avg_list, obp_list,
                                                 slg_list, ops_list, iso_list, spd_list, babip_list, wrc_list, wraa_list
                                                 , woba_list, wrc_plus_list):
            data = {
                'player': player['player'],
                'team_name': player['team'],
                'date': date.text,
                'team': team.text,
                'opp': opp.text,
                'bo': bo.text,
                'pos': pos.text,
                'bb_percentage': bb_percentage.text,
                'k_percentage': k_percentage.text,
                'bb_k': bb_k.text,
                'avg': avg.text,
                'obp': obp.text,
                'slg': slg.text,
                'ops': ops.text,
                'iso': iso.text,
                'spd': spd.text,
                'babip': babip.text,
                'wrc': wrc.text,
                'wraa': wraa.text,
                'woba': woba.text,
                'wrc_plus': wrc_plus.text
            }
            # print(data)
            headers = {'Content-type': 'application/json', 'Accept': '*/*'}
            requests.post(url='http://127.0.0.1:8000/core/dual-hitters-advanced/', data=json.dumps(data), headers=headers)

        players_scraped += 1
        print(f'Player scraped : {players_scraped}')

    except KeyboardInterrupt:
        driver.quit()
        break

    except Exception as e:
        print(f'Player : {player["player"]} | Team : {player["team"]}')
        print(f"Error :{e}")

driver.quit()
