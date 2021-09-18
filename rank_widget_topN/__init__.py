from otree.api import *


doc = """
"Widget to rank/reorder items". See http://sortablejs.github.io/Sortable/
for more examples.

The advantage of this one is that it requires the user to make an explicit choice,
rather than anchoring.
"""


class Constants(BaseConstants):
    name_in_url = 'rank_widget_topN'
    players_per_group = None
    num_rounds = 1
    choices = ['Martini', 'Margarita', 'White Russian', 'Pina Colada', 'Gin & Tonic']
    num_choices = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ranking = models.StringField()


def ranking_error_message(player: Player, value):
    """This is a backup in case the JS validation fails"""
    if len(value.split(',')) != Constants.num_choices:
        return "You must choose {} items".format(Constants.num_choices)


class MyPage(Page):
    form_model = 'player'
    form_fields = ['ranking']

    @staticmethod
    def js_vars(player: Player):
        return dict(NUM_CHOICES=Constants.num_choices)


class Results(Page):
    pass


page_sequence = [MyPage, Results]
