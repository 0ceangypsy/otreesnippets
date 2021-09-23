from otree.api import *


doc = """
Sequential game
"""


class Constants(BaseConstants):
    name_in_url = 'sequential'
    players_per_group = 3
    num_rounds = 1
    main_template = __name__ + '/Decide.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    mixer = models.StringField(
        choices=['Pineapple juice', 'Orange juice', 'Cola', 'Milk'],
        label="Choose a mixer",
        widget=widgets.RadioSelect,
    )
    liqueur = models.StringField(
        choices=['Blue curacao', 'Triple sec', 'Amaretto', 'Kahlua'],
        label="Choose a liqueur",
        widget=widgets.RadioSelect,
    )
    spirit = models.StringField(
        choices=['Vodka', 'Rum', 'Gin', 'Tequila'],
        label="Choose a spirit",
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):
    pass


# PAGES
class P1(Page):
    form_model = 'group'
    form_fields = ['mixer']
    template_name = Constants.main_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1


class WaitPage1(WaitPage):
    pass


class P2(Page):
    form_model = 'group'
    form_fields = ['liqueur']
    template_name = Constants.main_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2


class WaitPage2(WaitPage):
    pass


class P3(Page):
    form_model = 'group'
    form_fields = ['spirit']
    template_name = Constants.main_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 3


class WaitPage3(WaitPage):
    pass


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(players_with_contributions=group.get_players())


page_sequence = [P1, WaitPage1, P2, WaitPage2, P3, WaitPage3, Results]