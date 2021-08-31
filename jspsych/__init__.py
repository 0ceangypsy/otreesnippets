from otree.api import *


doc = """
It's easy to integrate with jsPsych, which means you can add all types of 
psychology tests to your experiments: https://www.jspsych.org/
"""


class Constants(BaseConstants):
    name_in_url = 'jspsych'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    avg_reaction = models.FloatField()
    jspsych_raw = models.LongStringField()


# FUNCTIONS
# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['avg_reaction', 'jspsych_raw']


class Results(Page):
    pass


page_sequence = [MyPage, Results]
