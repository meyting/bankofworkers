import random
from otree.api import *


doc = """
Your app description
"""
random.seed(10)

class C(BaseConstants):
    NAME_IN_URL = 'math_logic_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 100
    TIMER_TEXT = "Time to complete this section:"
    SEQUENCES_LOGIC = ['1, 5, 4, 8, 7, __ ', '12, 23, 34, 45, __ ', '15, 12, 9, 6, __ ', '2, 6, 4, 12, 10, 30, __',
                       '100, 99, 104, 103, 108, __', '2, 8, 14, 20, __', '64, 56, 48, 40, __',
                       '2, 5, 4, 7, 6, __', '120, 120, 60, 20, __ ', '1, 9, 2, 99, 3, 999, 4, 9999, __',
                       '8, 13, 18, 23, __ ', '2, 6, 10, 14, __', '18, 36, 72, 144, __', '7, 17, 27, 37, __',
                       '10, 15, 13, 18, __ ', '12, 10, 13, 11, 14, __', '1, 4, 9, 16, 25, __ ', '24, 34, 44, 54, __',
                       '88, 66, 44, 22, __', '22, 11, 44, 22, 88, __', '38, 34, 30, 26, __',
                       '1, 1, 2, 3, 5, 8, 13, __', '124, 62, 64, 32, 34, __', '2, 4, 6, 8, __',
                       '13, 4, 26, 8, 39, __', '21, 20, 18, 15, 11, __', '4, 12, 6, 18, 9, __',
                       '1, 1, 2, 6, 24, __', '50, 40, 31, 23, 16, __', '10, 11, 13, 16, 20, __',
                       '1, 3, 4, 6, 7, __', '53, 8, 54, 9, 55, 10, __', '2, 4, 3, 9, 4, 16, 5, __',
                       '87, 83, 79, 75, __', '10, 18, 26, 34, __', '101, 91, 81, 71, __', '95, 59, 85, 58, 75, __',
                       '3, 7, 11, 15, 19, __', '3, 4, 7, 11, 18, __', '9, 15, 21, 27, __', '27, 36, 45, 54, __',
                       '96, 48, 24, 12, __', '1, 3, 5, 7, __', '2, 4, 8, 16, __', '1, 2, 4, 7, 11, __',
                       '1, 3, 9, 27, __', '32, 26, 20, 14, __', '11, 22, 33, 44, __', '33, 38, 43, 48, __',
                       '1, 8, 27, 64, __']
    SOLUTIONS_LOGIC = [11, 56, 3, 28, 107, 26, 32, 9, 5, 5, 28, 18, 288, 47, 16, 12, 36, 64, 11, 44, 22, 21, 17, 10, 12,
                       6, 27, 120, 10, 25, 9, 56, 25, 71, 42, 61, 57, 23, 29, 33, 63, 6, 9, 32, 16, 81, 8, 55, 53, 125,]
    bonusrate = cu(0.05)
    bonusexample = 30
    bonusexample_math = 25
    bonusexample_logic = 35
    bonusexampleresult = bonusexample*bonusrate
    bonusexampleresult_logic = bonusexample_logic*bonusrate
    bonusexampleresult_math = bonusexample_math*bonusrate
    time_maths = 300
    time_maths_mins = round(time_maths/60)
    time_logic = 300
    time_logic_mins = round(time_logic/60)
    num_rounds_task = round(NUM_ROUNDS/2)
    lowest_integer = 0
    highest_integer = 10
    num_integers = 5

class Subsession(BaseSubsession):
    n1 = models.IntegerField()
    n2 = models.IntegerField()
    n3 = models.IntegerField()
    n4 = models.IntegerField()
    n5 = models.IntegerField()
    result_math = models.IntegerField()
    question_logic = models.StringField()
    result_logic = models.IntegerField()


import itertools
def creating_session(subsession):
    subsession.n1 = create_numbers(0)
    subsession.n2 = create_numbers(1)
    subsession.n3 = create_numbers(2)
    subsession.n4 = create_numbers(3)
    subsession.n5 = create_numbers(4)
    subsession.result_math = get_result(subsession.n1, subsession.n2, subsession.n3, subsession.n4, subsession.n5)
    if subsession.round_number == 1:
        for p in subsession.get_players():
            # 0 - 1.math 2.logic
            # 1 - 1.logic 2.math
            p.participant.total_points_math = 0
            p.participant.total_points_logic = 0
            p.task_first = p.participant.task_first
            solutions_logic = C.SOLUTIONS_LOGIC.copy()
            random.Random(0).shuffle(solutions_logic)
            solutions_logic.extend(solutions_logic)
            p.participant.solutions_logic = solutions_logic
            sequences_logic = C.SEQUENCES_LOGIC.copy()
            random.Random(0).shuffle(sequences_logic)
            sequences_logic.extend(sequences_logic)
            p.participant.sequences_logic = sequences_logic
    for p in subsession.get_players():
        p.solution_math = subsession.result_math
        subsession.question_logic = p.participant.sequences_logic[p.round_number - 1]
        subsession.result_logic = p.participant.solutions_logic[p.round_number - 1]
        p.solution_logic = subsession.result_logic



#            p.total_points_math = p.participant.total_points_math
#            p.total_points_logic = p.participant.total_points_logic



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    task_first = models.CharField()
    input_math = models.IntegerField(label='', blank=True)
    input_logic = models.IntegerField(label='', blank=True)
    solution_math = models.IntegerField()
    solution_logic = models.IntegerField()
    points_per_q_math = models.IntegerField(initial=0)
    points_per_q_logic = models.IntegerField(initial=0)
    total_points_math = models.IntegerField(initial=0)
    total_points_logic = models.IntegerField(initial=0)
    question_num_logic = models.IntegerField(initial=0)
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
        if participant.task_first == "math":
            return player.round_number == 1
        if participant.task_first == "logic":
            return player.round_number == C.num_rounds_task+1


class InstructionsLogic(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.task_first == "math":
            return player.round_number == C.num_rounds_task+1
        if participant.task_first == "logic":
            return player.round_number == 1


class StartMath(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.task_first == "math":
            return player.round_number == 1
        if participant.task_first == "logic":
            return player.round_number == C.num_rounds_task+1

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
        if participant.task_first == "math":
            return player.round_number == C.num_rounds_task+1
        if participant.task_first == "logic":
            return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + C.time_logic
        player.total_points_logic = 0


class QuestionsMath(Page):
    form_model = 'player'
    form_fields = ['input_math']
    get_timeout_seconds = get_timeout_seconds
    timer_text = C.TIMER_TEXT
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.task_first = participant.task_first
        print(player.task_first)
        if participant.task_first == "math":
            player.question_num_math = player.round_number
        else:
            player.question_num_math = player.round_number-C.num_rounds_task

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.field_maybe_none('input_math') == player.solution_math:
            player.points_per_q_math += 1
        participant = player.participant
        if player.field_maybe_none('input_math') == player.solution_math:
            participant.total_points_math += 1
        player.total_points_math = participant.total_points_math
        player.total_points_logic = participant.total_points_logic
        return player.total_points_math

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.task_first == "math":
            return player.round_number <= C.num_rounds_task and get_timeout_seconds(player) > 1
        if participant.task_first == "logic":
            return player.round_number > C.num_rounds_task and get_timeout_seconds(player) > 1


class QuestionsLogic(Page):
    form_model = 'player'
    form_fields = ['input_logic']
    get_timeout_seconds = get_timeout_seconds
    timer_text = C.TIMER_TEXT

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        player.task_first = participant.task_first
        print(player.task_first)
        if participant.task_first == "math":
            player.question_num_logic = player.round_number-C.num_rounds_task
        else:
            player.question_num_logic = player.round_number

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.field_maybe_none('input_logic') == player.solution_logic:
            player.points_per_q_logic += 1
        participant = player.participant
        if player.field_maybe_none('input_logic') == player.solution_logic:
            participant.total_points_logic += 1
        player.total_points_logic = participant.total_points_logic
        player.total_points_math = participant.total_points_math
        return player.total_points_logic

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        if participant.task_first == "logic":
            return player.round_number <= C.num_rounds_task and get_timeout_seconds(player) > 1
        if participant.task_first == "math":
            return player.round_number >  C.num_rounds_task and get_timeout_seconds(player) > 1

# result pages am Ende raus!!!
class ResultsMath(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


class ResultsLogic(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [InstructionsTask, InstructionsMath, InstructionsLogic, StartMath, StartLogic,
                 QuestionsMath, QuestionsLogic, ResultsMath, ResultsLogic]
