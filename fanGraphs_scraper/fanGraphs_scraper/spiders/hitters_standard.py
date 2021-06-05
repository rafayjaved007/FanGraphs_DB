import itertools
import json
import requests
from selenium import webdriver


def get_players():
    players_urls = []
    players = json.loads(requests.get(url='http://127.0.0.1:8000/core/hitters/?limit=150&offset=250').text)['results']

    for player in players:
        players_urls.append(player['url'])
    return players_urls, players


driver = webdriver.Firefox()
teams_scraped = 0

players = [{'player': 'Rafael Ortega', 'team': 'Cubs'}, {'player': 'Ketel Marte', 'team': 'D-backs'}, {'player': 'Matt Beaty', 'team': 'Dodgers'}]
urls = ['https://www.fangraphs.com/players/rafael-ortega/10323/stats?position=OF',
        'https://www.fangraphs.com/players/ketel-marte/13613/stats?position=2B/SS',
        'https://www.fangraphs.com/players/matt-beaty/17710/stats?position=1B/OF']
# urls, players = get_players()
for player_url, player in zip(urls, players):
    try:
        driver.get(player_url.replace("stats", "game-log"))

        s_url = driver.find_element_by_xpath(
            '//div[contains(@id,"content")]//ul[contains(@class,"menu-mega__game-log")]/li[2]/a').get_attribute("href")
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
        g_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='G']")[1:s]
        ab_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='AB']")[1:s]
        pa_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='PA']")[1:s]
        h_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='H']")[1:s]
        one_b_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='1B']")[1:s]
        two_b_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='2B']")[1:s]
        three_b_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='3B']")[1:s]
        hr_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='HR']")[1:s]
        r_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='R']")[1:s]
        rbi_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='RBI']")[1:s]
        bb_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BB']")[1:s]
        ibb_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='IBB']")[1:s]
        so_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='SO']")[1:s]
        hbp_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='HBP']")[1:s]
        sf_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='SF']")[1:s]
        sh_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='SH']")[1:s]
        gdp_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='GDP']")[1:s]
        sb_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='SB']")[1:s]
        cs_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='CS']")[1:s]
        avg_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='AVG']")[1:s]

        for date, team, opp, bo, pos, g, ab, pa, h, one_b, two_b, three_b, hr, r, rbi, bb, ibb, so, hbp, sf, sh, gdp,\
            sb, cs, avg in itertools.zip_longest(date_list[1:s], team_list, opp_list, bo_list, pos_list, g_list,
                                                 ab_list, pa_list, h_list, one_b_list, two_b_list, three_b_list, hr_list
                                                 , r_list, rbi_list, bb_list, ibb_list, so_list, hbp_list, sf_list,
                                                 sh_list, gdp_list, sb_list, cs_list, avg_list):
            data = {
                'player': player['player'],
                'team_name': player['team'],
                'date': date.text,
                'team': team.text,
                'opp': opp.text,
                'bo': bo.text,
                'pos': pos.text,
                'g': g.text,
                'ab': ab.text,
                'pa': pa.text,
                'h': h.text,
                '1b': one_b.text,
                '2b': two_b.text,
                '3b': three_b.text,
                'hr': hr.text,
                'r': r.text,
                'rbi': rbi.text,
                'bb': bb.text,
                'ibb': ibb.text,
                'so': so.text,
                'hbp': hbp.text,
                'sf': sf.text,
                'sh': sh.text,
                'gdp': gdp.text,
                'sb': sb.text,
                'cs': cs.text,
                'avg': avg.text,
            }
            headers = {'Content-type': 'application/json', 'Accept': '*/*'}
            requests.post(url='http://127.0.0.1:8000/core/hitters-standard/', data=json.dumps(data), headers=headers)

        teams_scraped += 1
        print(f'Players scraped : {teams_scraped}')

    except KeyboardInterrupt:
        driver.quit()
        break

    except Exception as e:
        print(f'Player : {player["player"]} | Team : {player["team"]}')
        print(f"Error :{e}")

driver.quit()
