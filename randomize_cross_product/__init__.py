from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'randomize_cross_product'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    import itertools

    treatments = itertools.cycle(
        [[True, True], [True, False], [False, True], [False, False]]
    )
    for player in subsession.get_players():
        treatment = next(treatments)
        player.time_pressure = treatment[0]
        player.high_tax = treatment[1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_pressure = models.BooleanField()
    high_tax = models.BooleanField()


class MyPage(Page):
    pass


page_sequence = [MyPage]
