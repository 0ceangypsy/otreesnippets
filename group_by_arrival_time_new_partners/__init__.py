from otree.api import *


doc = """
group by arrival time, but in each round assign to a new partner.
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


def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    session = subsession.session

    for p1 in waiting_players:
        for p2 in waiting_players:
            if p1 != p2:
                pair_ids = set([p1.id_in_subsession, p2.id_in_subsession])
                if pair_ids not in session.past_groups:
                    session.past_groups.append(pair_ids)
                    print('new pairing:', pair_ids)
                    return [p1, p2]
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
