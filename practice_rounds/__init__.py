from otree.api import *


doc = """Practice rounds"""


class Constants(BaseConstants):
    name_in_url = 'practice_rounds'
    players_per_group = None
    num_practice_rounds = 2
    num_real_rounds = 10
    num_rounds = num_practice_rounds + num_real_rounds


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response = models.IntegerField()
    solution = models.IntegerField()
    is_correct = models.BooleanField()


def is_practice_round(player: Player):
    return player.round_number <= Constants.num_practice_rounds


def real_round_number(player: Player):
    return player.round_number - Constants.num_practice_rounds


class Play(Page):
    form_model = 'player'
    form_fields = ['response']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            is_practice=is_practice_round(player),
            real_round_number=real_round_number(player),
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.solution = player.round_number ** 2
        player.is_correct = player.response == player.solution


class PracticeFeedback(Page):
    @staticmethod
    def is_displayed(player: Player):
        return is_practice_round(player)


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        score = sum(
            p.is_correct
            for p in player.in_rounds(
                Constants.num_practice_rounds + 1, Constants.num_rounds
            )
        )
        return dict(score=score)


page_sequence = [Play, PracticeFeedback, Results]
