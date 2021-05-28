# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScheduleItem(scrapy.Item):
    team = scrapy.Field()
    date = scrapy.Field()
    opp = scrapy.Field()
    team_win_prob = scrapy.Field()
    w_or_l = scrapy.Field()
    team_runs = scrapy.Field()
    opp_runs = scrapy.Field()
    team_starter = scrapy.Field()
    opp_starter = scrapy.Field()
