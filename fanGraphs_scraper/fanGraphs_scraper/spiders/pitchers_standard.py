import itertools
import json
import requests
from selenium import webdriver


def get_players():
    players_urls = []
    players = json.loads(requests.get(url='http://127.0.0.1:8000/core/pitchers/?limit=400&offset=34').text)['results']

    for player in players:
        players_urls.append(player['url'])
    return players_urls, players


driver = webdriver.Firefox()
teams_scraped = 0

players = [{'player': 'Shohei Ohtani', 'team': 'Angels'}]
urls = ['https://www.fangraphs.com/players/shohei-ohtani/19755/stats']
# urls, players = get_players()
for player_url, player in zip(urls, players):
    try:
        driver.get(player_url.replace("stats", "game-log"))
        print('Hello')

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
        gs_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='GS']")[1:s]
        w_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='W']")[1:s]
        l_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='L']")[1:s]
        era_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='ERA']")[1:s]
        g_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='G']")[1:s]
        cg_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='CG']")[1:s]
        sho_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='ShO']")[1:s]
        sv_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='SV']")[1:s]
        hld_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='HLD']")[1:s]
        bs_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BS']")[1:s]
        ip_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='IP']")[1:s]
        tbf_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='TBF']")[1:s]
        h_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='H']")[1:s]
        r_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='R']")[1:s]
        er_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='ER']")[1:s]
        hr_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='HR']")[1:s]
        bb_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BB']")[1:s]
        ibb_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='IBB']")[1:s]
        hbp_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='HBP']")[1:s]
        wp_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='WP']")[1:s]
        bk_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='BK']")[1:s]
        so_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='SO']")[1:s]
        gsv2_list = driver.find_elements_by_xpath("//div[@id='root-player-pages']//td[@data-stat='GSv2']")[1:s]

        for date, team, opp, gs, w, l, era, g, cg, sho, sv, hld,bs, ip, tbf, h, r, er, hr, bb, ibb, hbp, wp, bk, so, gsv2\
                in itertools.zip_longest(date_list[1:s], team_list, opp_list, gs_list, w_list, l_list, era_list,
                                         g_list, cg_list, sho_list, sv_list, hld_list, bs_list, ip_list, tbf_list
                                         , h_list, r_list, er_list, hr_list, bb_list, ibb_list, hbp_list,
                                         wp_list, bk_list, so_list, gsv2_list):
            data = {
                'player': player['player'],
                'team_name': player['team'],
                'date': date.text,
                'team': team.text,
                'opp': opp.text,
                'gs': gs.text,
                'w': w.text,
                'l': l.text,
                'era': era.text,
                'g': g.text,
                'cg': cg.text,
                'sho': sho.text,
                'sv': sv.text,
                'hld': hld.text,
                'bs': bs.text,
                'ip': ip.text,
                'tbf': tbf.text,
                'h': h.text,
                'r': r.text,
                'er': er.text,
                'hr': hr.text,
                'bb': bb.text,
                'ibb': ibb.text,
                'hbp': hbp.text,
                'wp': wp.text,
                'bk': bk.text,
                'so': so.text,
                'gsv2': gsv2.text,
            }
            # print(data)
            headers = {'Content-type': 'application/json', 'Accept': '*/*'}
            requests.post(url='http://127.0.0.1:8000/core/pitchers-standard/', data=json.dumps(data), headers=headers)

        teams_scraped += 1
        print(f'Players scraped : {teams_scraped}')

    except KeyboardInterrupt:
        driver.quit()
        break

    except Exception as e:
        print(f'Player : {player["player"]} | Team : {player["team"]}')
        print(f"Error :{e}")

driver.quit()
