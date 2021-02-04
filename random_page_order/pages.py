from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class TaskA(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['A']


class TaskB1(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['B']


class TaskB2(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['B']


class TaskC(Page):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['C']


page_sequence = [
    TaskA,
    TaskB1,
    TaskB2,
    TaskC,
]
