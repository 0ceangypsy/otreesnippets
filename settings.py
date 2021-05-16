from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.000, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='balance_treatments_for_dropouts',
        display_name='Assign a player to the treatment with the fewest datapoints',
        num_demo_participants=6,
        app_sequence=['balance_treatments_for_dropouts'],
    ),
    dict(
        name='complex_form_layout',
        num_demo_participants=1,
        app_sequence=['complex_form_layout'],
    ),
    dict(
        name='group_by_arrival_time_new_partners',
        display_name="group by arrival time, but in each round assign to a new partner.",
        num_demo_participants=16,
        app_sequence=['group_by_arrival_time_new_partners'],
    ),
    dict(
        name='groups_csv',
        display_name='Assign players to groups defined in a CSV file',
        num_demo_participants=6,
        app_sequence=['groups_csv'],
    ),
    dict(
        name='min_time_on_page',
        display_name='Minimum time on a page',
        num_demo_participants=1,
        app_sequence=['min_time_on_page'],
    ),
    dict(
        name='multi_select',
        display_name="Question that lets you select multiple options",
        num_demo_participants=1,
        app_sequence=['multi_select'],
    ),
    dict(
        name='other_player_previous_rounds',
        display_name="Showing other players' decisions from previous rounds",
        num_demo_participants=8,
        app_sequence=['other_player_previous_rounds'],
    ),
    dict(
        name='question_with_other_option',
        display_name="Menu with an 'other' option that lets you type in a value manually",
        num_demo_participants=4,
        app_sequence=['question_with_other_option'],
    ),
    dict(
        name='radio_switching_point',
        display_name='Radio button table with single switching point (strategy method)',
        num_demo_participants=4,
        app_sequence=['radio_switching_point'],
    ),
    dict(
        name='random_num_rounds',
        num_demo_participants=2,
        app_sequence=['random_num_rounds'],
    ),
    dict(
        name='random_page_order',
        display_name='Randomize page order',
        num_demo_participants=4,
        app_sequence=['random_page_order'],
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


DEMO_PAGE_INTRO_HTML = """
Recipes for common tasks in oTree
"""

# don't share this with anybody.
SECRET_KEY = 'fnv*lfr%ghepfge1rg1a56t0sj+9d*p&1+&g%q@j!ju@zu^v@6'

SESSION_FIELDS = ['completions_by_treatment', 'past_groups']
PARTICIPANT_FIELDS = ['partner_history', 'num_rounds']
