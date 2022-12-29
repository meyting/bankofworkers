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
    num_integers = 5
    example_math_n1 = 4
    example_math_n2 = 8
    example_math_n3 = 2
    example_math_n4 = 1
    example_math_n5 = 2
    result_math = example_math_n1+example_math_n2+example_math_n3+example_math_n4+example_math_n5

class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    import random
    import itertools
    tendency = itertools.cycle(['prowhite', 'problack', 'problack', 'prowhite'])
    if subsession.round_number == 1:
        for p in subsession.get_players():
            if 'tendency' in subsession.session.config:
                p.participant.tendency = subsession.session.config['tendency']
            else:
                p.participant.tendency = next(tendency)
            p.tendency = p.participant.tendency



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    tendency = models.StringField()


# PAGES

class Info(Page):
    pass


class Predictions(Page):
    pass



page_sequence = [Info,
                 Predictions
                 ]

