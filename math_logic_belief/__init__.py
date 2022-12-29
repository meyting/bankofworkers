from otree.api import *
import random


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'math_logic_belief'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    num_tasks = 3
    bonus = cu(0.3)
    examplebonus = 2*cu(0.3)
    bonusexample = 30
    num_rounds_task = 50
    samples = 100
    num_integers = 5
    limit = 2
    tasks = ["gender", "party", "race"]



class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    import random
    import itertools
    genderorder = itertools.cycle(['mf', 'fm'])
    partyorder = itertools.cycle(['dr', 'rd'])
    raceorder = itertools.cycle(['wahb', 'bhaw'])
    #cats = itertools.cycle(['pg', 'pr', 'rg', 'gp', 'rp', 'gr'])
    # gp --> pg ?
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1,C.num_tasks+1))
            random.shuffle(round_numbers)
            print(round_numbers)
            tasks = C.tasks.copy()
            random.shuffle(tasks)
            p.participant.task_rounds = dict(zip(tasks, round_numbers))
            print(p.participant.task_rounds)
            #if 'cats' in subsession.session.config:
            #    p.participant.cats = subsession.session.config['cats']
            #else:
            #    p.participant.cats = next(cats)
            #p.cats = p.participant.cats
            if 'genderorder' in subsession.session.config:
                p.participant.genderorder = subsession.session.config['genderorder']
            else:
                p.participant.genderorder = next(genderorder)
            p.genderorder = p.participant.genderorder
            if 'raceorder' in subsession.session.config:
                p.participant.raceorder = subsession.session.config['raceorder']
            else:
                p.participant.raceorder = next(raceorder)
            #p.genderoraceorder = p.participant.raceorder
            p.raceorder = p.participant.raceorder
            if 'partyorder' in subsession.session.config:
                p.participant.partyorder = subsession.session.config['partyorder']
            else:
                p.participant.partyorder = next(partyorder)
            p.partyorder = p.participant.partyorder

class Group(BaseGroup):
    pass


def make_field():
    return models.FloatField(
        label="",
        min=0,
        max=50,
        blank=True,
    )


class Player(BasePlayer):
    errors = models.IntegerField(blank=True, initial=0)
    math_first = models.BooleanField()
    cats = models.CharField()
    genderorder = models.StringField()
    raceorder= models.StringField()
    partyorder = models.StringField()
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


class Genderbeliefs(Page):
    form_model = 'player'
    form_fields = ['m_male1', 'm_male2', 'm_male3', 'm_female1', 'm_female2', 'm_female3',
                   'l_male1', 'l_male2', 'l_male3', 'l_female1', 'l_female2', 'l_female3',
                   ]

    @staticmethod
    def js_vars(player):
        return dict(
            genderorder=player.participant.genderorder,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.task_rounds["gender"]

    @staticmethod
    def error_message(player, values):
        try:
            if values['m_male1'] > values['m_male2']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 male participants should not be larger than the mean prediction for the best 10 male participants.'
            elif values['m_male1'] < values['m_male3']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 male participants should not be smaller than the mean prediction for the worst 10 male participants.'
            if values['m_female1'] > values['m_female2']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 female participants should not be larger than the mean prediction for the best 10 female participants.'
            elif values['m_female1'] < values['m_female3']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 female participants should not be smaller than the mean prediction for the worst 10 female participants.'
            if values['l_male1'] > values['l_male2']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 male participants should not be larger than the mean prediction for the best 10 male participants.'
            elif values['l_male1'] < values['l_male3']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 male participants should not be smaller than the mean prediction for the worst 10 male participants.'
            if values['l_female1'] > values['l_female2']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 female participants should not be larger than the mean prediction for the best 10 female participants.'
            elif values['l_female1'] < values['l_female3']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 female participants should not be smaller than the mean prediction for the worst 10 female participants.'
        except TypeError:
            player.errors += 1
            return "Please fill in all fields on this page."


class Racebeliefs(Page):
    form_model = 'player'
    form_fields = ['m_asian1', 'm_asian2','m_asian3', 'm_hispanic1', 'm_hispanic2', 'm_hispanic3',                    'm_white1', 'm_white2', 'm_white3', 'm_black1', 'm_black2', 'm_black3',
                   'l_asian1', 'l_asian2', 'l_asian3', 'l_hispanic1', 'l_hispanic2', 'l_hispanic3',
                   'm_white1', 'm_white2', 'm_white3', 'm_black1', 'm_black2', 'm_black3',
                   'l_white1', 'l_white2', 'l_white3', 'l_black1', 'l_black2', 'l_black3',
                   ]
    @staticmethod
    def js_vars(player):
        return dict(
            raceorder=player.participant.raceorder,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.task_rounds["race"]


    @staticmethod
    def error_message(player, values):
        print('values is', values)
        try:
            if values['m_asian1'] > values['m_asian2']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 Asian participants should not be larger than the mean prediction for the best 10 Asian participants.'
            elif values['m_asian1'] < values['m_asian3']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 Asian participants should not be smaller than the mean prediction for the worst 10 Asian participants.'
            if values['m_white1'] > values['m_white2']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 white participants should not be larger than the mean prediction for the best 10 white participants.'
            elif values['m_white1'] < values['m_white3']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 white participants should not be smaller than the mean prediction for the worst 10 white participants.'
            if values['m_hispanic1'] > values['m_hispanic2']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 Hispanic participants should not be larger than the mean prediction for the best 10 Hispanic participants.'
            elif values['m_hispanic1'] < values['m_hispanic3']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 Hispanic participants should not be smaller than the mean prediction for the worst 10 Hispanic participants.'
            if values['m_black1'] > values['m_black2']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 black participants should not be larger than the mean prediction for the best 10 black participants.'
            elif values['m_black1'] < values['m_black3']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 black participants should not be smaller than the mean prediction for the worst 10 black participants.'
            if values['l_asian1'] > values['l_asian2']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 Asian participants should not be larger than the mean prediction for the best 10 Asian participants.'
            elif values['l_asian1'] < values['l_asian3']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 Asian participants should not be smaller than the mean prediction for the worst 10 Asian participants.'
            if values['l_white1'] > values['l_white2']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 white participants should not be larger than the mean prediction for the best 10 white participants.'
            elif values['l_white1'] < values['l_white3']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 white participants should not be smaller than the mean prediction for the worst 10 white participants.'
            if values['l_hispanic1'] > values['l_hispanic2']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 Hispanic participants should not be larger than the mean prediction for the best 10 Hispanic participants.'
            elif values['l_hispanic1'] < values['l_hispanic3']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 Hispanic participants should not be smaller than the mean prediction for the worst 10 Hispanic participants.'
            if values['l_black1'] > values['l_black2']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 black participants should not be larger than the mean prediction for the best 10 black participants.'
            elif values['l_black1'] < values['l_black3']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 black participants should not be smaller than the mean prediction for the worst 10 black participants.'
        except TypeError:
            player.errors += 1
            return "Please fill in all fields on this page."


class Partybeliefs(Page):
    form_model = 'player'
    form_fields = ['m_democrat1', 'm_democrat2', 'm_democrat3', 'm_republican1', 'm_republican2', 'm_republican3',
                   'l_democrat1', 'l_democrat2', 'l_democrat3', 'l_republican1', 'l_republican2', 'l_republican3'
                   ]

    @staticmethod
    def js_vars(player):
        return dict(
            partyorder=player.participant.partyorder,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == player.participant.task_rounds["party"]


    @staticmethod
    def error_message(player, values):
        print('values is', values)
        try:
            if values['m_republican1'] > values['m_republican2']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 republican participants should not be larger than the mean prediction for the best 10 republican participants.'
            elif values['m_republican1'] < values['m_republican3']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 republican participants should not be smaller than the mean prediction for the worst 10 republican participants.'
            if values['m_democrat1'] > values['m_democrat2']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 democratic participants should not be larger than the mean prediction for the best 10 democratic participants.'
            elif values['m_democrat1'] < values['m_democrat3']:
                player.errors += 1
                return 'In the adding task, the mean prediction for all 100 democratic participants should not be smaller than the mean prediction for the worst 10 democratic participants.'
            if values['l_republican1'] > values['l_republican2']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 republican participants should not be larger than the mean prediction for the best 10 republican participants.'
            elif values['l_republican1'] < values['l_republican3']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 republican participants should not be smaller than the mean prediction for the worst 10 republican participants.'
            if values['l_democrat1'] > values['l_democrat2']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 democratic participants should not be larger than the mean prediction for the best 10 democratic participants.'
            elif values['l_democrat1'] < values['l_democrat3']:
                player.errors += 1
                return 'In the sequence task, the mean prediction for all 100 democratic participants should not be smaller than the mean prediction for the worst 10 democratic participants.'
        except TypeError:
            player.errors += 1
            return "Please fill in all fields on this page."

page_sequence = [InstructionsBeliefs,
                 Genderbeliefs,
                 Racebeliefs,
                 Partybeliefs,
                 #BeliefsMath, BeliefsLogic, BeliefsMath2
                 ]


'''

class BeliefsMath(Page):
    form_model = 'player'
    form_fields = ['m_male1', 'm_male2', 'm_male3', 'm_female1', 'm_female2', 'm_female3',
                   'm_asian1', 'm_asian2','m_asian3', 'm_hispanic1', 'm_hispanic2', 'm_hispanic3',
                   'm_white1', 'm_white2', 'm_white3', 'm_black1', 'm_black2', 'm_black3',
                   'm_democrat1','m_democrat2', 'm_democrat3', 'm_republican1', 'm_republican2', 'm_republican3']

    @staticmethod
    def js_vars(player):
        return dict(
            cats=player.participant.cats,
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.math_first

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['m_male1'] > values['m_male2']:
            player.errors += 1
            return 'The mean prediction for all 100 male participants should not be larger than the mean prediction for the best 10 male participants.'
        elif values['m_male1'] < values['m_male3']:
            player.errors += 1
            return 'The mean prediction for all 100 male participants should not be smaller than the mean prediction for the worst 10 male participants.'
        if values['m_female1'] > values['m_female2']:
            player.errors += 1
            return 'The mean prediction for all 100 female participants should not be larger than the mean prediction for the best 10 female participants.'
        elif values['m_female1'] < values['m_female3']:
            player.errors += 1
            return 'The mean prediction for all 100 female participants should not be smaller than the mean prediction for the worst 10 female participants.'
        if values['m_asian1'] > values['m_asian2']:
            player.errors += 1
            return 'The mean prediction for all 100 Asian participants should not be larger than the mean prediction for the best 10 Asian participants.'
        elif values['m_asian1'] < values['m_asian3']:
            player.errors += 1
            return 'The mean prediction for all 100 Asian participants should not be smaller than the mean prediction for the worst 10 Asian participants.'
        if values['m_white1'] > values['m_white2']:
            player.errors += 1
            return 'The mean prediction for all 100 white participants should not be larger than the mean prediction for the best 10 white participants.'
        elif values['m_white1'] < values['m_white3']:
            player.errors += 1
            return 'The mean prediction for all 100 white participants should not be smaller than the mean prediction for the worst 10 white participants.'
        if values['m_hispanic1'] > values['m_hispanic2']:
            player.errors += 1
            return 'The mean prediction for all 100 Hispanic participants should not be larger than the mean prediction for the best 10 Hispanic participants.'
        elif values['m_hispanic1'] < values['m_hispanic3']:
            player.errors += 1
            return 'The mean prediction for all 100 Hispanic participants should not be smaller than the mean prediction for the worst 10 Hispanic participants.'
        if values['m_black1'] > values['m_black2']:
            player.errors += 1
            return 'The mean prediction for all 100 black participants should not be larger than the mean prediction for the best 10 black participants.'
        elif values['m_black1'] < values['m_black3']:
            player.errors += 1
            return 'The mean prediction for all 100 black participants should not be smaller than the mean prediction for the worst 10 black participants.'
        if values['m_democrat1'] > values['m_democrat2']:
            player.errors += 1
            return 'The mean prediction for all 100 democratic participants should not be larger than the mean prediction for the best 10 democratic participants.'
        elif values['m_democrat1'] < values['m_democrat3']:
            player.errors += 1
            return 'The mean prediction for all 100 democratic participants should not be smaller than the mean prediction for the worst 10 democratic participants.'
        if values['m_republican1'] > values['m_republican2']:
            player.errors += 1
            return 'The mean prediction for all 100 republican participants should not be larger than the mean prediction for the best 10 republican participants.'
        elif values['m_republican1'] < values['m_republican3']:
            player.errors += 1
            return 'The mean prediction for all 100 republican participants should not be smaller than the mean prediction for the worst 10 republican participants.'


class BeliefsLogic(Page):
    form_model = 'player'
    form_fields = ['l_male1', 'l_male2', 'l_male3', 'l_female1', 'l_female2', 'l_female3',
                   'l_asian1', 'l_asian2', 'l_asian3', 'l_hispanic1', 'l_hispanic2', 'l_hispanic3',
                   'l_white1', 'l_white2', 'l_white3', 'l_black1', 'l_black2', 'l_black3',
                   'l_democrat1', 'l_democrat2', 'l_democrat3', 'l_republican1', 'l_republican2', 'l_republican3']

    @staticmethod
    def js_vars(player):
        return dict(
            cats=player.participant.cats,
        )

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['l_male1'] > values['l_male2']:
            player.errors += 1
            print(player.errors)
            return 'The mean prediction for all 100 male participants should not be larger than the mean prediction for the best 10 male participants.'
        elif values['l_male1'] < values['l_male3']:
            player.errors += 1
            return 'The mean prediction for all 100 male participants should not be smaller than the mean prediction for the worst 10 male participants.'
        if values['l_female1'] > values['l_female2']:
            player.errors += 1
            return 'The mean prediction for all 100 female participants should not be larger than the mean prediction for the best 10 female participants.'
        elif values['l_female1'] < values['l_female3']:
            player.errors += 1
            return 'The mean prediction for all 100 female participants should not be smaller than the mean prediction for the worst 10 female participants.'
        if values['l_asian1'] > values['l_asian2']:
            player.errors += 1
            return 'The mean prediction for all 100 Asian participants should not be larger than the mean prediction for the best 10 Asian participants.'
        elif values['l_asian1'] < values['l_asian3']:
            player.errors += 1
            return 'The mean prediction for all 100 Asian participants should not be smaller than the mean prediction for the worst 10 Asian participants.'
        if values['l_white1'] > values['l_white2']:
            player.errors += 1
            return 'The mean prediction for all 100 white participants should not be larger than the mean prediction for the best 10 white participants.'
        elif values['l_white1'] < values['l_white3']:
            player.errors += 1
            return 'The mean prediction for all 100 white participants should not be smaller than the mean prediction for the worst 10 white participants.'
        if values['l_hispanic1'] > values['l_hispanic2']:
            player.errors += 1
            return 'The mean prediction for all 100 Hispanic participants should not be larger than the mean prediction for the best 10 Hispanic participants.'
        elif values['l_hispanic1'] < values['l_hispanic3']:
            player.errors += 1
            return 'The mean prediction for all 100 Hispanic participants should not be smaller than the mean prediction for the worst 10 Hispanic participants.'
        if values['l_black1'] > values['l_black2']:
            player.errors += 1
            return 'The mean prediction for all 100 black participants should not be larger than the mean prediction for the best 10 black participants.'
        elif values['l_black1'] < values['l_black3']:
            player.errors += 1
            return 'The mean prediction for all 100 black participants should not be smaller than the mean prediction for the worst 10 black participants.'
        if values['l_democrat1'] > values['l_democrat2']:
            player.errors += 1
            return 'The mean prediction for all 100 democratic participants should not be larger than the mean prediction for the best 10 democratic participants.'
        elif values['l_democrat1'] < values['l_democrat3']:
            player.errors += 1
            return 'The mean prediction for all 100 democratic participants should not be smaller than the mean prediction for the worst 10 democratic participants.'
        if values['l_republican1'] > values['l_republican2']:
            player.errors += 1
            return 'The mean prediction for all 100 republican participants should not be larger than the mean prediction for the best 10 republican participants.'
        elif values['l_republican1'] < values['l_republican3']:
            player.errors += 1
            return 'The mean prediction for all 100 republican participants should not be smaller than the mean prediction for the worst 10 republican participants.'
 

class BeliefsMath2(Page):
    form_model = 'player'
    form_fields = ['m_male1', 'm_male2', 'm_male3', 'm_female1', 'm_female2', 'm_female3', 'm_asian1', 'm_asian2',
                   'm_asian3', 'm_hispanic1', 'm_hispanic2', 'm_hispanic3', 'm_democrat1',
                   'm_white1', 'm_white2', 'm_white3', 'm_black1', 'm_black2', 'm_black3',
                   'm_democrat2', 'm_democrat3', 'm_republican1', 'm_republican2', 'm_republican3']

    @staticmethod
    def js_vars(player):
        return dict(
            cats=player.participant.cats,
        )

    @staticmethod
    def is_displayed(player: Player):
        return not player.math_first

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['m_male1'] > values['m_male2']:
            player.errors += 1
            return 'The mean prediction for all 100 male participants should not be larger than the mean prediction for the best 10 male participants.'
        elif values['m_male1'] < values['m_male3']:
            player.errors += 1
            return 'The mean prediction for all 100 male participants should not be smaller than the mean prediction for the worst 10 male participants.'
        if values['m_female1'] > values['m_female2']:
            player.errors += 1
            return 'The mean prediction for all 100 female participants should not be larger than the mean prediction for the best 10 female participants.'
        elif values['m_female1'] < values['m_female3']:
            player.errors += 1
            return 'The mean prediction for all 100 female participants should not be smaller than the mean prediction for the worst 10 female participants.'
        if values['m_asian1'] > values['m_asian2']:
            player.errors += 1
            return 'The mean prediction for all 100 Asian participants should not be larger than the mean prediction for the best 10 Asian participants.'
        elif values['m_asian1'] < values['m_asian3']:
            player.errors += 1
            return 'The mean prediction for all 100 Asian participants should not be smaller than the mean prediction for the worst 10 Asian participants.'
        if values['m_white1'] > values['m_white2']:
            player.errors += 1
            return 'The mean prediction for all 100 white participants should not be larger than the mean prediction for the best 10 white participants.'
        elif values['m_white1'] < values['m_white3']:
            player.errors += 1
            return 'The mean prediction for all 100 white participants should not be smaller than the mean prediction for the worst 10 white participants.'
        if values['m_hispanic1'] > values['m_hispanic2']:
            player.errors += 1
            return 'The mean prediction for all 100 Hispanic participants should not be larger than the mean prediction for the best 10 Hispanic participants.'
        elif values['m_hispanic1'] < values['m_hispanic3']:
            player.errors += 1
            return 'The mean prediction for all 100 Hispanic participants should not be smaller than the mean prediction for the worst 10 Hispanic participants.'
        if values['m_black1'] > values['m_black2']:
            player.errors += 1
            return 'The mean prediction for all 100 black participants should not be larger than the mean prediction for the best 10 black participants.'
        elif values['m_black1'] < values['m_black3']:
            player.errors += 1
            return 'The mean prediction for all 100 black participants should not be smaller than the mean prediction for the worst 10 black participants.'
        if values['m_democrat1'] > values['m_democrat2']:
            player.errors += 1
            return 'The mean prediction for all 100 democratic participants should not be larger than the mean prediction for the best 10 democratic participants.'
        elif values['m_democrat1'] < values['m_democrat3']:
            player.errors += 1
            return 'The mean prediction for all 100 democratic participants should not be smaller than the mean prediction for the worst 10 democratic participants.'
        if values['m_republican1'] > values['m_republican2']:
            player.errors += 1
            return 'The mean prediction for all 100 republican participants should not be larger than the mean prediction for the best 10 republican participants.'
        elif values['m_republican1'] < values['m_republican3']:
            player.errors += 1
            return 'The mean prediction for all 100 republican participants should not be smaller than the mean prediction for the worst 10 republican participants.'
'''