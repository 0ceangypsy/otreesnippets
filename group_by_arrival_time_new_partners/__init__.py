from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'group_by_arrival_time_new_partners'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    session.past_groups = []


def get_pair_ids(waiting_players):
    return set(p.participant.id_in_session for p in waiting_players)


def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    session = subsession.session
    import itertools

    for possible_group in itertools.combinations(waiting_players, 2):
        pair_ids = get_pair_ids(possible_group)
        if pair_ids not in session.past_groups:
            session.past_groups.append(pair_ids)
            print('new pairing:', pair_ids)
            return possible_group
        else:
            print('already played together:', pair_ids)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class ResultsWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "Waiting to pair you with someone you haven't already played with"


class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(partner=player.get_others_in_group()[0])


page_sequence = [ResultsWaitPage, MyPage]
