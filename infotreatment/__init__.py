from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'infotreatment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    bonusrate = cu(0.03)
    time_sequence_mins = 5
    time_math_mins = 4
    num_rounds_task = 50
    sample = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES

class Info(Page):
    pass


class Predictions(Page):
    pass



page_sequence = [Info,
                 Predictions
                 ]

