from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
For each participant, randomize the order of tasks A, B, and C.
Task B has 2 pages, which are always shown in the same order.
The page_sequence contains all tasks;
in each round we show a randomly determined subset of pages.
"""

class Constants(BaseConstants):
    name_in_url = 'random_page_order'
    players_per_group = None
    tasks = ['A', 'B', 'C']
    num_rounds = len(tasks)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds+1))
                random.shuffle(round_numbers)
                p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
