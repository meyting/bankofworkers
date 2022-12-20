from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolificid = models.CharField(initial=None,
                                  verbose_name="Before we start, please provide your Prolific ID.")

# PAGES
class Instructions(Page):
    form_model = 'player'
    form_fields = ['prolificid']

page_sequence = [Instructions]
