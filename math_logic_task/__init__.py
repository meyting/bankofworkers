import random
from otree.api import *


doc = """
Your app description
"""
random.seed(0)

class C(BaseConstants):
    NAME_IN_URL = 'math_logic_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 100
    TIMER_TEXT = "Remaining time for this task:"
    SEQUENCES_sequence = ['1 , 5 , 4 , 8 , 7 , ', '12 , 23 , 34 , 45 , ', '15 , 12 , 9 , 6 , ',
                          '2 , 6 , 4 , 12 , 10 , 30 , ',
                          '100 , 99 , 104 , 103 , 108 , ', '2 , 8 , 14 , 20 , ', '64 , 56 , 48 , 40 , ',
                          '2 , 5 , 4 , 7 , 6 , ', '120 , 120 , 60 , 20 , ', '1 , 9 , 2 , 99 , 3 , 999 , 4 , 9999 , ',
                          '8 , 13 , 18 , 23 , ', '2 , 6 , 10 , 14 , ', '18 , 36 , 72 , 144 , ', '7 , 17 , 27 , 37 , ',
                          '10 , 15 , 13 , 18 , ', '12 , 10 , 13 , 11 , 14 , ', '1 , 4 , 9 , 16 , 25 , ',
                          '24 , 34 , 44 , 54 , ',
                          '88 , 66 , 44 , 22 , ', '22 , 11 , 44 , 22 , 88 , ', '18 , 14 , 10 , 6 , ',
                          '1 , 1 , 2 , 3 , 5 , 8 , 13 , ', '124 , 62 , 64 , 32 , 34 , ', '2 , 4 , 6 , 8 , ',
                          '13 , 4 , 26 , 8 , 39 , ', '21 , 20 , 18 , 15 , 11 , ', '4 , 12 , 6 , 18 , 9 , ',
                          '1 , 1 , 2 , 6 , 24 , ', '50 , 40 , 31 , 23 , 16 , ', '10 , 11 , 13 , 16 , 20 , ',
                          '1 , 3 , 4 , 6 , 7 , ', '53 , 8 , 54 , 9 , 55 , 10 , ', '2 , 4 , 3 , 9 , 4 , 16 , ',
                          '27 , 23 , 19 , 15 , ', '10 , 18 , 26 , 34 , ', '101 , 91 , 81 , 71 , ',
                          '95 , 59 , 85 , 58 , 75 , ', '3 , 7 , 11 , 15 , 19 , ', '3 , 4 , 7 , 11 , 18 , ',
                          '9 , 15 , 21 , 27 , ', '9 , 18 , 27 , 36 , ',
                          '96 , 48 , 24 , 12 , ', '1 , 3 , 5 , 7 , ', '2  , 4  , 8  , 16  , ', '1 , 2 , 4 , 7 , 11 , ',
                          '1 , 3 , 9 , 27 , ', '32 , 26 , 20 , 14 , ', '11 , 22 , 33 , 44 , ', '10 , 15 , 20 , 25 , ',
                          '1 , 8 , 27 , 64 , ']
    example_math_n1 = 4
    example_math_n2 = 8
    example_math_n3 = 2
    example_math_n4 = 1
    example_math_n5 = 2
    result_math = example_math_n1+example_math_n2+example_math_n3+example_math_n4+example_math_n5
    SOLUTIONS_sequence = [11, 56, 3, 28, 107, 26, 32, 9, 5, 5, 28, 18, 288, 47, 16, 12, 36, 64, 11, 44, 2, 21, 17, 10,
                          12, 6, 27, 120, 10, 25, 9, 56, 5, 11, 42, 61, 57, 23, 29, 33, 45, 6, 9, 32, 16, 81, 8, 55, 30,
                          125, ]
    bonusrate = cu(0.03)
    bonusexample = 30
    bonusexample_math = 25
    bonusexample_sequence = 35
    bonusexampleresult = bonusexample*bonusrate
    bonusexampleresult_sequence = bonusexample_sequence*bonusrate
    bonusexampleresult_math = bonusexample_math*bonusrate
    time_maths = 240
    time_maths_mins = round(time_maths/60)
    time_sequence = 300
    time_sequence_mins = round(time_sequence/60)
    num_rounds_task = round(NUM_ROUNDS/2)
    lowest_integer = 1
    highest_integer = 10
    num_integers = 5

class Subsession(BaseSubsession):
    n1 = models.IntegerField()
    n2 = models.IntegerField()
    n3 = models.IntegerField()
    n4 = models.IntegerField()
    n5 = models.IntegerField()
    result_math = models.IntegerField()
    question_sequence = models.StringField()
    result_sequence = models.IntegerField()


import itertools
def creating_session(subsession):
    if subsession.round_number <= 50:
        subsession.n1 = create_numbers(0)
        subsession.n2 = create_numbers(1)
        subsession.n3 = create_numbers(2)
        subsession.n4 = create_numbers(3)
        subsession.n5 = create_numbers(4)
    if subsession.round_number > 50:
        subsession.n1 = subsession.in_round(subsession.round_number-50).n1
        subsession.n2 = subsession.in_round(subsession.round_number-50).n2
        subsession.n3 = subsession.in_round(subsession.round_number-50).n3
        subsession.n4 = subsession.in_round(subsession.round_number-50).n4
        subsession.n5 = subsession.in_round(subsession.round_number-50).n5
    subsession.result_math = get_result(subsession.n1, subsession.n2, subsession.n3, subsession.n4, subsession.n5)
    if subsession.round_number == 1:
        for p in subsession.get_players():
            # 0 - 1.math 2.sequence
            # 1 - 1.sequence 2.math
            p.participant.total_points_math = 0
            p.participant.total_points_sequence = 0
            p.task = p.participant.task
            solutions_sequence = C.SOLUTIONS_sequence.copy()
            #random.Random(0).shuffle(solutions_sequence)
            solutions_sequence.extend(solutions_sequence)
            p.participant.solutions_sequence = solutions_sequence
            sequences_sequence = C.SEQUENCES_sequence.copy()
            #random.Random(0).shuffle(sequences_sequence)
            sequences_sequence.extend(sequences_sequence)
            p.participant.sequences_sequence = sequences_sequence
    for p in subsession.get_players():
        #if p.participant.task == "math":
#        if p.participant.task == "sequence":
#            random_numbers = random.Random(p.round_number-50).sample(range(0,10),5)
#            print("sequence",random_numbers)
        p.solution_math = subsession.result_math
        subsession.question_sequence = p.participant.sequences_sequence[p.round_number - 1]
        subsession.result_sequence = p.participant.solutions_sequence[p.round_number - 1]
        p.solution_sequence = subsession.result_sequence



#            p.total_points_math = p.participant.total_points_math
#            p.total_points_sequence = p.participant.total_points_sequence



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task = models.CharField()
    input_math = models.IntegerField(label='', blank=True)
    input_sequence = models.IntegerField(label='', blank=True)
    solution_math = models.IntegerField()
    solution_sequence = models.IntegerField()
    points_per_q_math = models.IntegerField(initial=0)
    points_per_q_sequence = models.IntegerField(initial=0)
    total_points_math = models.IntegerField(initial=0)
    total_points_sequence = models.IntegerField(initial=0)
    question_num_sequence = models.IntegerField(initial=0)
    question_num_math = models.IntegerField(initial=0)


def create_numbers(i):
    random_numbers = [random.randint(1, 10) for x in range(5)]
    return random_numbers[i]


def get_result(x1, x2, x3, x4, x5):
    result = x1 + x2 + x3 + x4 + x5
    return result


def get_timeout_seconds(player):
    participant = player.participant
    import time
    return participant.expiry - time.time()


# PAGES
class InstructionsTask(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class InstructionsMath (Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.task == "math"


class InstructionsLogic(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.task == "sequence"


class StartMath(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.task == "math"

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + C.time_maths
        player.total_points_math = 0

class StartLogic(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.task == "sequence"

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + C.time_sequence
        player.total_points_sequence = 0

class QuestionsMath(Page):
    form_model = 'player'
    form_fields = ['input_math']
    get_timeout_seconds = get_timeout_seconds
    timer_text = C.TIMER_TEXT
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.task = participant.task
        print(player.task)
        player.question_num_sequence = player.round_number
        return {
                "n1": player.subsession.n1,
                "n2": player.subsession.n2,
                "n3": player.subsession.n3,
                "n4": player.subsession.n4,
                "n5": player.subsession.n5
            }

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.field_maybe_none('input_math') == player.solution_math:
            player.points_per_q_math += 1
        participant = player.participant
        if player.field_maybe_none('input_math') == player.solution_math:
            participant.total_points_math += 1
        player.total_points_math = participant.total_points_math
        player.total_points_sequence = participant.total_points_sequence
        return player.total_points_math

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.task == "math"



class QuestionsLogic(Page):
    form_model = 'player'
    form_fields = ['input_sequence']
    get_timeout_seconds = get_timeout_seconds
    timer_text = C.TIMER_TEXT

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.task = participant.task
        player.question_num_sequence = player.round_number

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.field_maybe_none('input_sequence') == player.solution_sequence:
            player.points_per_q_sequence += 1
        participant = player.participant
        if player.field_maybe_none('input_sequence') == player.solution_sequence:
            participant.total_points_sequence += 1
        player.total_points_sequence = participant.total_points_sequence
        player.total_points_math = participant.total_points_math
        return player.total_points_sequence

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return participant.task == "sequence"

page_sequence = [#InstructionsTask,
                 InstructionsMath,
                 InstructionsLogic,
                 StartMath,
                 StartLogic,
                 QuestionsMath, QuestionsLogic,]
