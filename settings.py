from os import environ

SESSION_CONFIGS = [
    dict(
        name='alles',
        app_sequence=['welcome','instructions', 'math_logic_task', 'math_logic_belief', 'self_estimation', 'survey','end'],
        num_demo_participants=20,
    ),
    dict(
        name='mathe_logic_test',
        app_sequence=['welcome','math_logic_task'],
        num_demo_participants=4,
    ),
    dict(
        name='beliefs',
        app_sequence=['welcome','math_logic_belief'],
        num_demo_participants=10,
    ),
    dict(
        name='selfest',
        app_sequence=['self_estimation'],
        num_demo_participants=10,
    ),
    dict(
        name='survey',
        app_sequence=['survey'],
        num_demo_participants=3,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['expiry', 'total_points_math', 'task_first', 'belief_treatment', 'task_rounds',
                      'total_points_sequence', "sequences_sequence", "solutions_sequence",
                      'raceorder', "partyorder", "genderorder",]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'bankofworkers'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'bankofworkers'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '2964019777290'

AUTH_LEVEL = 'STUDY' # wieder löschen wenn Umgebungsvariable gesetzt			!!!!!!!!!!!!!!!
