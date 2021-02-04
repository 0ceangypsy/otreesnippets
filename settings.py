from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.000, participation_fee=0.00, doc="")

SESSION_CONFIGS = [
    dict(name='random_page_order', display_name='Randomize page order', num_demo_participants=4,
         app_sequence=['random_page_order']),
    dict(name='radio_switching_point', display_name='Radio button table with single switching point (strategy method)',
         num_demo_participants=4, app_sequence=['radio_switching_point']),
    dict(name='groups_csv', display_name='Assign players to groups defined in a CSV file', num_demo_participants=6,
         app_sequence=['groups_csv'])
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

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
