from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.000, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='getattr_setattr',
        num_demo_participants=1,
        app_sequence=['getattr_setattr'],
    ),
    dict(
        name='are_you_sure',
        display_name="""'Are you sure?' popup based on the user's input""",
        num_demo_participants=1,
        app_sequence=['are_you_sure'],
    ),
    dict(
        name='balance_treatments_for_dropouts',
        display_name='Assign a player to the treatment with the fewest datapoints',
        num_demo_participants=6,
        app_sequence=['balance_treatments_for_dropouts'],
    ),
    dict(
        name='groups_csv',
        display_name='Assign players to groups defined in a CSV file',
        num_demo_participants=6,
        app_sequence=['groups_csv'],
    ),
    dict(
        name='back_button',
        display_name='Back button for multiple instructions pages',
        num_demo_participants=1,
        app_sequence=['back_button'],
    ),
    dict(
        name='bmi_calculator',
        display_name='Basic 1-player game (BMI calculator)',
        num_demo_participants=1,
        app_sequence=['bmi_calculator'],
    ),
    dict(
        name='detect_mobile',
        display_name='Block mobile browsers',
        num_demo_participants=1,
        app_sequence=['detect_mobile'],
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
        name='constant_sum',
        display_name="Constant-sum input (3 numbers that add up to 100)",
        num_demo_participants=1,
        app_sequence=['constant_sum'],
    ),
    dict(
        name='configurable_players_per_group',
        display_name="Configurable players_per_group (doesn't work in demo mode)",
        num_demo_participants=12,
        app_sequence=['configurable_players_per_group'],
        players_per_group=3,
    ),
    dict(
        name='count_button_clicks',
        display_name='Count button clicks (hidden input)',
        num_demo_participants=1,
        app_sequence=['count_button_clicks'],
    ),
    dict(
        name='css',
        num_demo_participants=1,
        app_sequence=['css'],
        display_name="CSS to style timer and chat box",
    ),
    dict(
        name='custom_chat',
        display_name="Custom chat (not using oTree's built-in chat)",
        num_demo_participants=3,
        app_sequence=['custom_chat'],
    ),
    dict(
        name='dropout_detection',
        display_name='Dropout detection (if user does not submit page in time)',
        num_demo_participants=1,
        app_sequence=['dropout_detection'],
    ),
    dict(
        name='gbat_new_partners',
        display_name="group by arrival time, but in each round assign to a new partner.",
        num_demo_participants=16,
        app_sequence=['gbat_new_partners'],
    ),
    dict(
        name='gbat_keep_same_groups',
        display_name="group_by_arrival_time: Preserve same groups as a previous app that used group_by_arrival_time.",
        num_demo_participants=6,
        app_sequence=[
            'gbat_keep_same_groups_part0',
            'gbat_keep_same_groups_part1',
            'gbat_keep_same_groups_part2',
        ],
    ),
    dict(
        name='waiting_too_long',
        display_name="group_by_arrival_time timeout (continue with solo task)",
        num_demo_participants=2,
        app_sequence=[
            'waiting_too_long_part0',
            'waiting_too_long_part1',
            'waiting_too_long_part2',
        ],
    ),
    dict(
        name='history_table',
        display_name='History table',
        num_demo_participants=1,
        app_sequence=['history_table'],
    ),
    dict(
        name='longitudinal',
        display_name='Longitudinal study (2-part study taking place across days/weeks)',
        num_demo_participants=1,
        app_sequence=['longitudinal'],
    ),
    dict(
        name='question_with_other_option',
        display_name="Menu with an 'other' option that lets you type in a value manually",
        num_demo_participants=4,
        app_sequence=['question_with_other_option'],
    ),
    dict(
        name='min_time_on_page',
        display_name='Minimum time on a page',
        num_demo_participants=1,
        app_sequence=['min_time_on_page'],
    ),
    dict(
        name='pass_data_between_apps',
        display_name='Pass data between apps',
        num_demo_participants=1,
        app_sequence=['pass_data_between_apps_part1', 'pass_data_between_apps_part2'],
    ),
    dict(
        name='pay_random_round',
        display_name="Pay a randomly selected round",
        num_demo_participants=1,
        app_sequence=['pay_random_round'],
    ),
    dict(
        name='practice_rounds',
        display_name="Practice rounds",
        app_sequence=['practice_rounds'],
        num_demo_participants=1,
    ),
    dict(
        name='progress_bar',
        display_name="Progress bar",
        num_demo_participants=1,
        app_sequence=['progress_bar'],
    ),
    dict(
        name='multi_select',
        display_name="Question that lets you select multiple options",
        num_demo_participants=1,
        app_sequence=['multi_select'],
    ),
    dict(
        name='questions_from_csv',
        display_name='Quiz questions loaded from CSV spreadsheet + custom_export',
        num_demo_participants=2,
        app_sequence=['questions_from_csv'],
    ),
    dict(
        name='quiz_with_explanation',
        display_name="Quiz + post-quiz explanation. Re-display the previous page's form as read-only, with answers/explanation.",
        num_demo_participants=1,
        app_sequence=['quiz_with_explanation'],
    ),
    dict(
        name='radio_switching_point',
        display_name='Radio button table with single switching point (strategy method)',
        num_demo_participants=1,
        app_sequence=['radio_switching_point'],
    ),
    dict(
        name='radio',
        display_name="Radio buttons in various layouts, looping over radio choices",
        app_sequence=['radio'],
        num_demo_participants=1,
    ),
    dict(
        name='random_num_rounds',
        display_name="Random number of rounds",
        num_demo_participants=2,
        app_sequence=['random_num_rounds'],
    ),
    dict(
        name='random_num_rounds_multiplayer',
        display_name="Random number of rounds for multiplayer (random stopping rule)",
        num_demo_participants=2,
        app_sequence=[
            'random_num_rounds_multiplayer',
            'random_num_rounds_multiplayer_end',
        ],
    ),
    dict(
        name='randomize_cross_product',
        display_name="Randomize multiple factors in a balanced way",
        num_demo_participants=16,
        app_sequence=['randomize_cross_product'],
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
        name='rank_widget',
        display_name="Rank/reorder form widget",
        num_demo_participants=1,
        app_sequence=['rank_widget'],
    ),
    dict(
        name='rank_topN',
        display_name="Ranking your top N choices from a list of options.",
        num_demo_participants=1,
        app_sequence=['rank_topN'],
    ),
    dict(
        name='redirect_to_other_website',
        display_name="Redirect the user to another website and pass their data",
        num_demo_participants=1,
        app_sequence=['redirect_to_other_website'],
    ),
    dict(
        name='appcopy',
        display_name='Sandwich design (App A -> App B -> App A)',
        num_demo_participants=1,
        app_sequence=['appcopy1', 'multi_select', 'appcopy2'],
    ),
    dict(
        name='sequential',
        display_name="""Sequential game""",
        num_demo_participants=3,
        app_sequence=['sequential'],
    ),
    dict(
        name='other_player_previous_rounds',
        display_name="Showing other players' decisions from previous rounds",
        num_demo_participants=8,
        app_sequence=['other_player_previous_rounds'],
    ),
    dict(
        name='slider_live_label',
        display_name="Slider with live updating label",
        num_demo_participants=1,
        app_sequence=['slider_live_label'],
    ),
    dict(
        name='slider_graphic',
        display_name="Slider that changes an image (e.g. happy to sad scale)",
        num_demo_participants=1,
        app_sequence=['slider_graphic'],
    ),
    dict(
        name='slider_checkbox_reloadable',
        display_name="Sliders and checkboxes that don't get wiped out on form reload.",
        app_sequence=['slider_checkbox_reloadable'],
        num_demo_participants=1,
    ),
    dict(
        name='wait_page_timeout',
        display_name="Timeout on a WaitPage (exit the experiment)",
        num_demo_participants=2,
        app_sequence=['wait_page_timeout'],
    ),
    dict(
        name='multi_page_timeout',
        display_name="Timeout spanning multiple pages",
        num_demo_participants=1,
        app_sequence=['multi_page_timeout'],
    ),
    dict(
        name='multi_language',
        display_name="Translate an app to multiple languages (e.g. English and German)",
        num_demo_participants=1,
        app_sequence=['multi_language'],
    ),
    dict(
        name='treatments_from_spreadsheet',
        display_name="Treatments defined in a spreadsheet",
        num_demo_participants=12,
        app_sequence=['treatments_from_spreadsheet'],
    ),
    dict(
        name='wait_for_specific_people',
        display_name="Wait only for specific people",
        num_demo_participants=8,
        app_sequence=['wait_for_specific_people'],
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
    'wait_for_ids',
    'arrived_ids',
]

PARTICIPANT_FIELDS = [
    'expiry',
    'finished_rounds',
    'language',
    'num_rounds',
    'partner_history',
    'past_group_id',
    'progress',
    'selected_round',
    'task_rounds',
    'wait_page_arrival',
]
