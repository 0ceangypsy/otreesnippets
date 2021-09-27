from otree.api import *


doc = """
Image choices with radio buttons
"""


def make_image_data(images):
    return [dict(name=name, path='shapes/{}'.format(name)) for name in images]


class Constants(BaseConstants):
    name_in_url = 'image_choices'
    players_per_group = None
    num_rounds = 1
    image_names = [
        'circle-blue.svg',
        'plus-green.svg',
        'star-red.svg',
        'triangle-yellow.svg',
    ]
    image_data = make_image_data(image_names)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    img_choice = models.StringField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['img_choice']

    @staticmethod
    def error_message(player: Player, values):
        return 'aa'


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
