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


class StartingLineUpItem(scrapy.Item):
    pos = scrapy.Field()
    player = scrapy.Field()
    bats = scrapy.Field()
    power_rank_ovr = scrapy.Field()
    power_rank_last_7_days = scrapy.Field()
    lineup_1 = scrapy.Field()
    lineup_2 = scrapy.Field()
    lineup_3 = scrapy.Field()
    lineup_4 = scrapy.Field()
    lineup_5 = scrapy.Field()
    lineup_6 = scrapy.Field()

