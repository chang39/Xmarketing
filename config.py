class Config(object):
    PROJECT_NAME = 'michelangelo'
    PROFILE='default'

class DevConfig(Config):
    DATABASE_URI = 'mysql://dementor:Messi#10@127.0.0.1:3306/test?charset=utf8'
    LOG_FILE = '/Users/dementor/Documents/logs/xmarketing/website.log'
    CRON_LOG_FILE = '/Users/dementor/Documents/logs/xmarketing/cron.log'
    PROFILE='dev'

class TestConfig(Config):
    DATABASE_URI = 'mysql://dementor:Messi%4010@127.0.0.1:3306/michelangelo?charset=utf8'
    LOG_FILE = '/Users/dementor/Documents/logs/xmarketing/website.log'
    CRON_LOG_FILE = '/Users/dementor/Documents/logs/xmarketing/cron.log'
    PROFILE='test'
