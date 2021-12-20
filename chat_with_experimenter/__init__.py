from otree.api import *


doc = """
Chat with experimenter, using Papercups
"""


class C(BaseConstants):
    NAME_IN_URL = 'chat_with_experimenter'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PAPERCUPS_TEMPLATE = __name__ + '/papercups.html'


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
