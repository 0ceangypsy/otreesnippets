from otree.api import *

c = Currency

doc = """
Minimum time on a page
"""


class Constants(BaseConstants):
    name_in_url = 'min_time_on_page'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass




page_sequence = [MyPage]
