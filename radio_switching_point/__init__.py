from otree.api import (
    Page,
    WaitPage,
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from . import models


doc = """
Table where each row has a left/right choice,
like the strategy method.
This app enforces a single switching point
"""


class Constants(BaseConstants):
    name_in_url = 'radio_switching_point'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    left_side_amount = models.CurrencyField(initial=10)
    switching_point = models.CurrencyField()


# FUNCTIONS
def right_side_amounts(player: Player):
    return currency_range(10, 20, 1)


# PAGES
class Decide(Page):
    form_model = 'player'
    form_fields = ['switching_point']

    @staticmethod
    def vars_for_template(player):
        return dict(right_side_amounts=right_side_amounts(player))


class Results(Page):
    pass


page_sequence = [Decide, Results]
