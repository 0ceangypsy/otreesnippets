import csv
from pprint import pprint

from otree.api import (
    Page,
    WaitPage,
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
Reads groups from a CSV file.
Inside this app, you will find a groups6.csv,
which defines the groups in the case where there are 6 players.
You can edit the file in Excel, or in plain text.
In the below example, there are 5 rows, defining 5 rounds. 
In each row, empty cells are used to separate groups. 
So, in round 1, there are 3 groups: players 1&4, 2&5, 3&6:
1,4,,2,5,,3,6
1,2,,3,4,,6,5
1,3,,6,2,,5,4
1,6,,5,3,,4,2
1,5,,4,6,,2,3
If you want to create a session with a different number of players, 
such as 12, you would need to create a file called groups12.csv.
"""


def make_group(comma_delim_string):
    return [int(x) for x in comma_delim_string.split(',')]


class Constants(BaseConstants):
    name_in_url = 'groups_csv'
    players_per_group = None
    num_rounds = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        num_participants = subsession.session.num_participants
        fn = 'groups_csv/groups{}.csv'.format(num_participants)
        with open(fn) as f:
            matrices = []
            for line in f:
                line = line.strip()
                group_specs = line.split(',,')
                matrix = [make_group(spec) for spec in group_specs]
                matrices.append(matrix)
            subsession.session.vars['matrices'] = matrices
    this_round_matrix = subsession.session.vars['matrices'][subsession.round_number - 1]
    subsession.set_group_matrix(this_round_matrix)
    pprint(this_round_matrix)


# PAGES
class MyPage(Page):
    pass


page_sequence = [
    MyPage,
]
