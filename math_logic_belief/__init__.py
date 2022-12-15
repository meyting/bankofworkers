from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'math_logic_belief'
    PLAYERS_PER_GROUP = None
    TASKS = ['BeliefsMath', 'BeliefsLogic']
    NUM_ROUNDS = len(TASKS)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.TASKS, round_numbers))
            p.participant.task_rounds = task_rounds
            p.task_math_pos = p.participant.task_rounds["BeliefsMath"]
            p.task_logic_pos = p.participant.task_rounds["BeliefsLogic"]
            # saves "1" if the corr. task is first or "2" if second (beliefs)
            p.participant.belief_treatment = random.randint(0, 1)
            p.belief_treatment = p.participant.belief_treatment
            # belief_treatment 0: men-women asians-hispanics democrats-republicans
            # treatment 1: je vv
            # --> noch alle Optionen einfügen (8?) + ggf noch Kategorien in unterschiedliche Rhf.???


class Group(BaseGroup):
    pass


def make_field():
    return models.IntegerField(
        label="",
        min=0,
        max=50
    )


class Player(BasePlayer):
    belief_treatment = models.IntegerField()
    task_math_pos = models.IntegerField()
    task_logic_pos = models.IntegerField()
    m_male1 = make_field()
    m_male2 = make_field()
    m_male3 = make_field()
    m_female1 = make_field()
    m_female2 = make_field()
    m_female3 = make_field()
    m_asian1 = make_field()
    m_asian2 = make_field()
    m_asian3 = make_field()
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


class InstructionsMathB(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['BeliefsMath']


class InstructionsLogicB(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['BeliefsLogic']


class BeliefsMath(Page):
    form_model = 'player'
    form_fields = ['m_male1', 'm_male2', 'm_male3', 'm_female1', 'm_female2', 'm_female3', 'm_asian1', 'm_asian2',
                   'm_asian3', 'm_hispanic1', 'm_hispanic2', 'm_hispanic3', 'm_democrat1',
                   'm_democrat2', 'm_democrat3', 'm_republican1', 'm_republican2', 'm_republican3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['BeliefsMath'] and participant.belief_treatment == 0


class BeliefsMath2(Page):
    form_model = 'player'
    form_fields = ['m_male1', 'm_male2', 'm_male3', 'm_female1', 'm_female2', 'm_female3', 'm_asian1', 'm_asian2',
                   'm_asian3', 'm_hispanic1', 'm_hispanic2', 'm_hispanic3', 'm_democrat1',
                   'm_democrat2', 'm_democrat3', 'm_republican1', 'm_republican2', 'm_republican3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['BeliefsMath'] and participant.belief_treatment == 1


class BeliefsLogic(Page):
    form_model = 'player'
    form_fields = ['l_male1', 'l_male2', 'l_male3', 'l_female1', 'l_female2', 'l_female3',
                   'l_asian1', 'l_asian2', 'l_asian3', 'l_hispanic1', 'l_hispanic2', 'l_hispanic3',
                   'l_democrat1', 'l_democrat2', 'l_democrat3', 'l_republican1', 'l_republican2', 'l_republican3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['BeliefsLogic'] and participant.belief_treatment == 0


class BeliefsLogic2(Page):
    form_model = 'player'
    form_fields = ['l_male1', 'l_male2', 'l_male3', 'l_female1', 'l_female2', 'l_female3',
                   'l_asian1', 'l_asian2', 'l_asian3', 'l_hispanic1', 'l_hispanic2', 'l_hispanic3',
                   'l_democrat1', 'l_democrat2', 'l_democrat3', 'l_republican1', 'l_republican2', 'l_republican3']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['BeliefsLogic'] and participant.belief_treatment == 1

    #@staticmethod
    #def error_message(player, value):
     #   print('value is', value)
      #  if value['l_male1'] <= -1 or value['l_male1'] >= 51:
       #     return 'Please type in a number between 0 and 50'


page_sequence = [InstructionsBeliefs, BeliefsMath, BeliefsMath2, BeliefsLogic, BeliefsLogic2]