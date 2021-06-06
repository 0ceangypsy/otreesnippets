from otree.api import *


doc = """
'Are you sure?' popup based on the user's input
"""


class Constants(BaseConstants):
    name_in_url = 'are_you_sure'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=100, label="How much of your 100 points do you want to contribute?"
    )
    reason = models.LongStringField(
        blank=True,
        label="Please write a message to your teammates explaining your decision",
    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['contribution', 'reason']


page_sequence = [MyPage]
