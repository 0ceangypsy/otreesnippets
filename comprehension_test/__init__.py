from otree.api import *

doc = """
Comprehension test. If the user fails too many times, they exit.
"""


class Constants(BaseConstants):
    name_in_url = 'comprehension_test'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
    quiz1 = models.IntegerField(label='What is 19 + 23?')
    quiz2 = models.StringField(label='What is the capital of Canada?')
    quiz3 = models.IntegerField(
        label="What year was Barack Obama first elected president?"
    )
    quiz4 = models.BooleanField(
        label="Was Thomas Jefferson the first president of the USA?"
    )


class MyPage(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']

    @staticmethod
    def error_message(player: Player, values):
        # alternatively, you could make quiz1_error_message, quiz2_error_message, etc.
        # but if you have many similar fields, this is more efficient.
        solutions = dict(quiz1=42, quiz2='Ottawa', quiz3=2008, quiz4=False)

        errors = {f: 'Wrong' for f in solutions if values[f] != solutions[f]}
        # if you don't care about failed attempts, just put:
        # return errors
        # otherwise, do this:
        if errors:
            player.num_failed_attempts += 1
            if player.num_failed_attempts >= 3:
                player.failed_too_many = True
            else:
                return errors


class Failed(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many


class Results(Page):
    pass


page_sequence = [MyPage, Failed, Results]
