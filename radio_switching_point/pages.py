from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decide(Page):
    form_model = 'player'
    form_fields = ['switching_point']


class Results(Page):
    pass


page_sequence = [
    Decide,
    Results
]
