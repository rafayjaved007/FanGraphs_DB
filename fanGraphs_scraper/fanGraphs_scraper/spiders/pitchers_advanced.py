import itertools
import json
import requests
from selenium import webdriver


def get_players():
    players_urls = []
    players = json.loads(requests.get(url='http://127.0.0.1:8000/core/pitchers/').text)['results']

    for player in players:
        players_urls.append(player['url'])
    return players_urls, players


driver = webdriver.Firefox()
players_scraped = 0
urls, players = get_players()
for player_url, player in zip(urls, players):
    try:
        driver.get(player_url.replace("stats", "game-log"))

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
        gs_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='GS']")[1:s]
        k_9_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='K/9']")[1:s]
        bb_9_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BB/9']")[1:s]
        k_bb_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='K/BB']")[1:s]
        hr_9_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='HR/9']")[1:s]
        k_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='K%']")[1:s]
        bb_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BB%']")[1:s]
        k_bb_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='K-BB%']")[1:s]
        avg_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='AVG']")[1:s]
        whip_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='WHIP']")[1:s]
        babip_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BABIP']")[1:s]
        lob_percentage_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='LOB%']")[1:s]
        era_dash_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='ERA-']")[1:s]
        fip_dash_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='FIP-']")[1:s]
        fip_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='FIP']")[1:s]

        for date, team, opp, gs, k_9, bb_9, k_bb, hr_9, k_percentage, bb_percentage, k_bb_percentage, avg, whip, babip,\
                lob_percentage, era_dash, fip_dash, fip in itertools.zip_longest(date_list[1:s], team_list, opp_list,
                                                         gs_list, k_9_list, bb_9_list, k_bb_list, hr_9_list,
                                                         k_percentage_list, bb_percentage_list, k_bb_percentage_list,
                                                         avg_list, whip_list, babip_list, lob_percentage_list,
                                                         era_dash_list, fip_dash_list, fip_list):
            data = {
                'player': player['player'],
                'team_name': player['team'],
                'date': date.text,
                'team': team.text,
                'opp': opp.text,
                'gs': gs.text,
                'k_9': k_9.text,
                'bb_9': bb_9.text,
                'k_bb': k_bb.text,
                'hr_9': hr_9.text,
                'k_percentage': k_percentage.text,
                'bb_percentage': bb_percentage.text,
                'k_bb_percentage': k_bb_percentage.text,
                'avg': avg.text,
                'whip': whip.text,
                'babip': babip.text,
                'lob_percentage': lob_percentage.text,
                'era_dash': era_dash.text,
                'fip_dash': fip_dash.text,
                'fip': fip.text
            }
            print(data)
            # headers = {'Content-type': 'application/json', 'Accept': '*/*'}
            # requests.post(url='http://127.0.0.1:8000/core/hitters-advanced/', data=json.dumps(data), headers=headers)

        players_scraped += 1
        print(f'Player scraped : {players_scraped}')

    except KeyboardInterrupt:
        driver.quit()
        break

    except Exception as e:
        print(f'Player : {player["player"]} | Team : {player["team"]}')
        print(f"Error :{e}")

driver.quit()
