from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'math_logic_belief'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    bonus = cu(1)
    bonusexample = 30
    num_rounds_task = 50
    samples = 100
    num_integers = 5


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    import itertools
    cats = itertools.cycle(['grp', 'prg', 'rgp', 'pgr', 'gpr', 'rpg'])
    if subsession.round_number == 1:
        for p in subsession.get_players():
            if p.participant.task_first == "math":
                p.math_first = True
            else:
                p.math_first = False
            if 'cats' in subsession.session.config:
                p.participant.cats = subsession.session.config['cats']
            else:
                p.participant.cats = next(cats)
            p.cats = p.participant.cats

class Group(BaseGroup):
    pass


def make_field():
    return models.IntegerField(
        label="",
        min=0,
        max=50,
        blank=True,
    )


class Player(BasePlayer):
    math_first = models.BooleanField()
    cats = models.CharField()
    m_male1 = make_field()
    m_male2 = make_field()
    m_male3 = make_field()
    m_female1 = make_field()
    m_female2 = make_field()
    m_female3 = make_field()
    m_asian1 = make_field()
    m_asian2 = make_field()
    m_asian3 = make_field()
    m_white1 = make_field()
    m_white2 = make_field()
    m_white3 = make_field()
    m_black1 = make_field()
    m_black2 = make_field()
    m_black3 = make_field()
    m_hispanic1 = make_field()
    m_hispanic2 = make_field()
    m_hispanic3 = make_field()
    m_democrat1 = make_field()
    m_democrat2 = make_field()
    m_democrat3 = make_field()
    m_republican1 = make_field()
    m_republican2 = make_field()
    m_republican3 = make_field()
    l_male1 = make_field()
    l_male2 = make_field()
    l_male3 = make_field()
    l_female1 = make_field()
    l_female2 = make_field()
    l_female3 = make_field()
    l_asian1 = make_field()
    l_asian2 = make_field()
    l_asian3 = make_field()
    l_black1 = make_field()
    l_black2 = make_field()
    l_black3 = make_field()
    l_white1 = make_field()
    l_white2 = make_field()
    l_white3 = make_field()
    l_hispanic1 = make_field()
    l_hispanic2 = make_field()
    l_hispanic3 = make_field()
    l_democrat1 = make_field()
    l_democrat2 = make_field()
    l_democrat3 = make_field()
    l_republican1 = make_field()
    l_republican2 = make_field()
    l_republican3 = make_field()


# PAGES
class InstructionsBeliefs(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class BeliefsMath(Page):
    form_model = 'player'
    form_fields = ['m_male1', 'm_male2', 'm_male3', 'm_female1', 'm_female2', 'm_female3',
                   'm_asian1', 'm_asian2','m_asian3', 'm_hispanic1', 'm_hispanic2', 'm_hispanic3',
                   'm_white1', 'm_white2', 'm_white3', 'm_black1', 'm_black2', 'm_black3',
                   'm_democrat1','m_democrat2', 'm_democrat3', 'm_republican1', 'm_republican2', 'm_republican3']

    @staticmethod
    def is_displayed(player: Player):
        return player.math_first


class BeliefsLogic(Page):
    form_model = 'player'
    form_fields = ['l_male1', 'l_male2', 'l_male3', 'l_female1', 'l_female2', 'l_female3',
                   'l_asian1', 'l_asian2', 'l_asian3', 'l_hispanic1', 'l_hispanic2', 'l_hispanic3',
                   'l_white1', 'l_white2', 'l_white3', 'l_black1', 'l_black2', 'l_black3',
                   'l_democrat1', 'l_democrat2', 'l_democrat3', 'l_republican1', 'l_republican2', 'l_republican3']


class BeliefsMath2(Page):
    form_model = 'player'
    form_fields = ['m_male1', 'm_male2', 'm_male3', 'm_female1', 'm_female2', 'm_female3', 'm_asian1', 'm_asian2',
                   'm_asian3', 'm_hispanic1', 'm_hispanic2', 'm_hispanic3', 'm_democrat1',
                   'm_white1', 'm_white2', 'm_white3', 'm_black1', 'm_black2', 'm_black3',
                   'm_democrat2', 'm_democrat3', 'm_republican1', 'm_republican2', 'm_republican3']

    @staticmethod
    def is_displayed(player: Player):
        return not player.math_first




    #@staticmethod
    #def error_message(player, value):
     #   print('value is', value)
      #  if value['l_male1'] <= -1 or value['l_male1'] >= 51:
       #     return 'Please type in a number between 0 and 50'


page_sequence = [InstructionsBeliefs, BeliefsMath, BeliefsLogic, BeliefsMath2]