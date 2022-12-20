from otree.api import *
import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'welcome'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    import itertools
    task_first = itertools.cycle(['sequence', 'math'])
    if subsession.round_number == 1:
        for p in subsession.get_players():
            if 'task_first' in subsession.session.config:
                p.participant.task_first = subsession.session.config['task_first']
            else:
                p.participant.task_first = next(task_first)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField()
    prolificid = models.CharField(initial=None,
                                  verbose_name="Before we start, please provide your Prolific ID.")

# PAGES
class consent(Page):
    form_model = 'player'
    form_fields = ['consent']

class instructions(Page):
    form_model = 'player'
    form_fields = ['prolificid']

page_sequence = [consent,
                 ]
