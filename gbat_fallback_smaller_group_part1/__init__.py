from otree.api import *

doc = """
group_by_arrival_time: fall back to a smaller group if not enough people show up
"""


class Constants(BaseConstants):
    name_in_url = 'gbat_fallback_smaller_group_part1'
    players_per_group = 4
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def waiting_seconds(player):
    import time

    participant = player.participant
    return time.time() - participant.wait_page_arrival


def num_waiting_longer_than(waiting_players, num_minutes):
    count = 0
    for p in waiting_players:
        # FIXME: remove the .1, just for debugging
        if waiting_seconds(p) >= num_minutes * 60:
            count += 1
    return count


def group_by_arrival_time_method(subsession, waiting_players):
    print("number of players waiting:", len(waiting_players))
    # ideally we can play in groups of 4...
    if len(waiting_players) >= 4:
        print("Creating a group of 4! Ideal!")
        return waiting_players[:4]
    if num_waiting_longer_than(waiting_players, num_minutes=1) >= 3:
        print(
            "3 players have been waiting for a short time, so we settle for a group of 3"
        )
        return waiting_players
    if num_waiting_longer_than(waiting_players, num_minutes=2) >= 2:
        print(
            "2 players have been waiting for a really long time, so we group whoever is waiting"
        )
        return waiting_players
    # etc...


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    favorite_color = models.StringField()


class GBAT(WaitPage):
    group_by_arrival_time = True


class GroupTask(Page):
    form_model = 'player'
    form_fields = ['favorite_color']


class MyWait(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [GBAT, GroupTask, MyWait, Results]
