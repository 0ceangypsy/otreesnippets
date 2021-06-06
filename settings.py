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
        name='appcopy',
        display_name='Sandwich design (App A -> App B -> App A)',
        num_demo_participants=1,
        app_sequence=['appcopy1', 'multi_select', 'appcopy2'],
    ),
    dict(
        name='are_you_sure',
        display_name="""'Are you sure?' popup based on the user's input""",
        num_demo_participants=1,
        app_sequence=['are_you_sure'],
    ),
    dict(
        name='back_button',
        display_name='Back button for multiple instructions pages',
        num_demo_participants=1,
        app_sequence=['back_button'],
    ),
    dict(
        name='balance_treatments_for_dropouts',
        display_name='Assign a player to the treatment with the fewest datapoints',
        num_demo_participants=6,
        app_sequence=['balance_treatments_for_dropouts'],
    ),
    dict(
        name='chat_with_experimenter',
        display_name="Chat with experimenter",
        num_demo_participants=1,
        app_sequence=['chat_with_experimenter'],
    ),
    dict(
        name='complex_form_layout',
        display_name="Complex form layout",
        num_demo_participants=1,
        app_sequence=['complex_form_layout'],
    ),
    dict(
        name='comprehension_test',
        display_name="Comprehension test (quiz you must pass to proceed)",
        num_demo_participants=1,
        app_sequence=['comprehension_test'],
    ),
    dict(
        name='count_button_clicks',
        display_name='Count button clicks (hidden input)',
        num_demo_participants=1,
        app_sequence=['count_button_clicks'],
    ),
    dict(
        name='detect_mobile',
        display_name='Block mobile browsers',
        num_demo_participants=1,
        app_sequence=['detect_mobile'],
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
        name='history_table',
        display_name='History table',
        num_demo_participants=1,
        app_sequence=['history_table'],
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
        name='multi_page_timeout',
        display_name="Timeout spanning multiple pages",
        num_demo_participants=1,
        app_sequence=['multi_page_timeout'],
    ),
    dict(
        name='other_player_previous_rounds',
        display_name="Showing other players' decisions from previous rounds",
        num_demo_participants=8,
        app_sequence=['other_player_previous_rounds'],
    ),
    dict(
        name='pass_data_between_apps',
        display_name='Pass data between apps',
        num_demo_participants=1,
        app_sequence=['pass_data_between_apps1', 'pass_data_between_apps2'],
    ),
    dict(
        name='question_with_other_option',
        display_name="Menu with an 'other' option that lets you type in a value manually",
        num_demo_participants=4,
        app_sequence=['question_with_other_option'],
    ),
    dict(
        name='questions_from_csv',
        display_name='Quiz questions loaded from CSV spreadsheet + custom_export',
        num_demo_participants=2,
        app_sequence=['questions_from_csv'],
    ),
    dict(
        name='radio_switching_point',
        display_name='Radio button table with single switching point (strategy method)',
        num_demo_participants=4,
        app_sequence=['radio_switching_point'],
    ),
    dict(
        name='random_num_rounds',
        display_name="Random number of rounds",
        num_demo_participants=2,
        app_sequence=['random_num_rounds'],
    ),
    dict(
        name='randomize_cross_product',
        display_name="Randomize multiple factors in a balanced way",
        num_demo_participants=16,
        app_sequence=['randomize_cross_product'],
    ),
    dict(
        name='ranking_widget',
        display_name="Widget to rank/reorder items",
        num_demo_participants=1,
        app_sequence=['ranking_widget'],
    ),
    dict(
        name='random_question_order',
        display_name='Randomize order of questions',
        num_demo_participants=4,
        app_sequence=['random_question_order'],
    ),
    dict(
        name='random_task_order',
        display_name='Randomize order of different tasks',
        num_demo_participants=4,
        app_sequence=['random_task_order'],
    ),
    dict(
        name='redirect_to_other_website',
        display_name="Redirect the user to another website and pass their data",
        num_demo_participants=1,
        app_sequence=['redirect_to_other_website'],
    ),
    dict(
        name='slider_live_label',
        display_name="Slider with live updating label",
        num_demo_participants=1,
        app_sequence=['slider_live_label'],
    ),
    dict(
        name='waiting_too_long',
        display_name="group_by_arrival_time timeout (continue with solo task)",
        num_demo_participants=2,
        app_sequence=[
            'waiting_too_long_screening',
            'waiting_too_long',
            'waiting_too_long_solo',
        ],
    ),
    dict(
        name='wait_page_timeout',
        display_name="Timeout on a WaitPage (exit the experiment)",
        num_demo_participants=2,
        app_sequence=['wait_page_timeout'],
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


DEMO_PAGE_TITLE = """
Recipes for common tasks in oTree
"""

DEMO_PAGE_INTRO_HTML = """
Recipes for common tasks in oTree
"""


# don't share this with anybody.
SECRET_KEY = 'fnv*lfr%ghepfge1rg1a56t0sj+9d*p&1+&g%q@j!ju@zu^v@6'

SESSION_FIELDS = [
    'completions_by_treatment',
    'past_groups',
    'matrices',
]

PARTICIPANT_FIELDS = [
    'partner_history',
    'num_rounds',
    'language',
    'wait_page_arrival',
    'expiry',
    'task_rounds',
]