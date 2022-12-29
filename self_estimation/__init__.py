from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'self_estimation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    num_rounds_task = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    est_math = models.IntegerField(
        min=0,
        max=50,
        blank = True,
    )
    est_avg_math = models.BooleanField(
        label='Do you think you achieved a higher score in the adding task than the average of all participants in our study?',
        choices=[[0, 'yes'], [1, 'no']],
        widget=widgets.RadioSelectHorizontal(),
        blank = True
    )
    est_sequence = models.IntegerField(
        min=0,
        max=50,
        blank=True
    )
    est_avg_sequence = models.IntegerField(
        label="Do you think you achieved a higher score in the sequence task than the average of all participants in our study? ",
        choices=[[0, 'yes'], [1, 'no']],
        widget=widgets.RadioSelectHorizontal(),
        blank=True,
    )


# PAGES
class SelfEstimation(Page):
    form_model = 'player'
    form_fields = ['est_math', 'est_avg_math', 'est_sequence', 'est_avg_sequence']


page_sequence = [SelfEstimation]
