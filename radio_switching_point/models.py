from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


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

    def right_side_amounts(self):
        return currency_range(10, 20, 1)
