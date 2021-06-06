from otree.api import *

doc = """Count button clicks (hidden input)"""

class Constants(BaseConstants):
    name_in_url = 'count_button_clicks'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_clicks = models.IntegerField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['num_clicks']


class Results(Page):
    pass


page_sequence = [MyPage, Results]
