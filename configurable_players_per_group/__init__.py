from otree.api import *


doc = """
Configurable players per group.
See here: https://otree.readthedocs.io/en/latest/treatments.html#configure-sessions
"""


class Constants(BaseConstants):
    name_in_url = 'configurable_players_per_group'
    # Since Constants does not have access to the session config,
    # (it is loaded when the server starts, rather than for each session)
    # we set the groups manually inside creating_session.
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    ppg = session.config['players_per_group']
    players = subsession.get_players()
    matrix = []
    for i in range(0, len(players), ppg):
        matrix.append(players[i : i + ppg])
    subsession.set_group_matrix(matrix)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class MyPage(Page):
    pass


page_sequence = [MyPage]
