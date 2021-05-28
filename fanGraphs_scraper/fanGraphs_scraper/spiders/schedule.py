import scrapy
import requests
import json
import urllib.parse as urlparse
from urllib.parse import parse_qs
import itertools
from ..items import ScheduleItem


class NoonSpider(scrapy.Spider):
    name = "schedule_spider"


    def get_teams():
        urls = []
        teams = json.loads(requests.get(url='http://127.0.0.1:8000/core/team/').text)['results']

        for team_name in teams:
            urls.append(f'https://www.fangraphs.com/teams/{team_name["name"].lower().replace(" ", "-")}/schedule')
        return urls

    start_urls = get_teams()

    def parse(self, response):
        items = ScheduleItem()
        pre_xpath = '//div[contains(@class,"team-schedule-table")]/table/tr/td'
        url = response.xpath(f'{pre_xpath}[1]/a/@href').extract_first()
        parsed = urlparse.urlparse(url)
        team = parse_qs(parsed.query)['team'][0]

        date_list = response.xpath(f'{pre_xpath}[1]//span[1]/text()').extract()
        opp_list = response.xpath(f'{pre_xpath}[3]//text()').extract()
        team_win_prob_list = response.xpath(f'{pre_xpath}[4]//text()').extract()
        w_or_l_list = response.xpath(f'{pre_xpath}[5]//text()').extract()
        team_runs_list = response.xpath(f'{pre_xpath}[6]//text()').extract()
        opp_runs_list = response.xpath(f'{pre_xpath}[7]//text()').extract()
        team_starter_list = response.xpath(f'{pre_xpath}[8]//text()').extract()
        opp_starter_list = response.xpath(f'{pre_xpath}[9]//text()').extract()

        for date,opp,team_win_prob,w_or_l,team_runs,opp_runs,team_starter,opp_starter in \
                itertools.zip_longest(date_list,opp_list,team_win_prob_list,w_or_l_list,team_runs_list,opp_runs_list,
                                      team_starter_list,opp_starter_list):
            items['team'] = team
            items['date'] = date
            items['opp'] = opp
            items['team_win_prob'] = team_win_prob
            items['w_or_l'] = w_or_l
            items['team_runs'] = team_runs
            items['opp_runs'] = opp_runs
            items['team_starter'] = team_starter
            items['opp_starter'] = opp_starter

            # data = {"team": "Blue Jays", "date": "Apr 1, 2021", "opp": "NYY", "team_win_prob": "39.0%", "w_or_l": "W", "team_runs": "3", "opp_runs": "2", "team_starter": "Hyun Jin Ryu", "opp_starter": "Gerrit Cole"}


            # print(json.dumps(dict(items)))
            headers = {'Content-type': 'application/json', 'Accept': '*/*'}
            requests.post(url='http://127.0.0.1:8000/core/schedule/', data=json.dumps(dict(items)), headers=headers)

            # yield requests.post(data=team=team,date=date,opp=opp,team_win_prob=team_win_prob,w_or_l=w_or_l,
            #                     team_runs=team_runs,opp_runs=opp_runs,team_starter=team_starter,opp_starter=opp_starter)

