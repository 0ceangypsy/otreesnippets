from otree.api import *


doc = """
Sequential game
"""


class Constants(BaseConstants):
    name_in_url = 'sequential'
    players_per_group = 3
    num_rounds = 1
    contribute_template = __name__ + '/Contribute.html'
    table_template = __name__ + '/table.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    contribution = models.CurrencyField(label="How much do you want to contribute?")


def vars_for_template(player: Player):
    return dict(
        players_with_contributions=[
            other
            for other in player.get_others_in_group()
            if other.id_in_group < player.id_in_group
        ]
    )


# PAGES
class P1(Page):
    form_model = 'player'
    form_fields = ['contribution']
    template_name = Constants.contribute_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

    vars_for_template = vars_for_template


class WaitPage1(WaitPage):
    pass


class P2(Page):
    form_model = 'player'
    form_fields = ['contribution']
    template_name = Constants.contribute_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    vars_for_template = vars_for_template


class WaitPage2(WaitPage):
    pass


class P3(Page):
    form_model = 'player'
    form_fields = ['contribution']
    template_name = Constants.contribute_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 3

    vars_for_template = vars_for_template


class WaitPage3(WaitPage):
    pass


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(players_with_contributions=group.get_players())


page_sequence = [P1, WaitPage1, P2, WaitPage2, P3, WaitPage3, Results]
