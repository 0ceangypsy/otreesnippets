from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'waiting_too_long_part0'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        import time
        participant.wait_page_arrival = time.time()


page_sequence = [MyPage]
