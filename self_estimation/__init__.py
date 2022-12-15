from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'self_estimation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    est_math = models.IntegerField(
        label='How many of the 50 questions in the <b> math task </b> do you think you have answered correctly?',
        min=0,
        max=50,
    )
    est_avg_math = models.BooleanField(
        label='Do you think you achieved a higher score in the <b> math task </b> than the average of all participants in our experiment?',
        choices=[[0, 'yes'], [1, 'no']],
        widget=widgets.RadioSelectHorizontal()
    )
    est_logic = models.IntegerField(
        label='How many of the 50 questions in the <b> logic task </b> do you think you have answered correctly?',
        min=0,
        max=50,
    )
    est_avg_logic = models.IntegerField(
        label="Do you think you achieved a higher score in the <b> logic task </b> than the average of all participants in our experiment? ",
        choices=[[0, 'yes'], [1, 'no']],
        widget=widgets.RadioSelectHorizontal()
    )


# PAGES
class SelfEstimation(Page):
    form_model = 'player'
    form_fields = ['est_math', 'est_avg_math', 'est_logic', 'est_avg_logic']


page_sequence = [SelfEstimation]
