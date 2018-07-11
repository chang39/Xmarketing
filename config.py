class Config(object):
    PROJECT_NAME = 'michelangelo'
    PROFILE='default'

class DevConfig(Config):
    DATABASE_URI = 'mysql://dementor:Messi#10@127.0.0.1:3306/test?charset=utf8'
    UPLOAD_FOLDER = '/Users/dementor/Documents/upload/xmarketing'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    PIC_URL = 'http://p3atcmc03.bkt.clouddn.com/'
    AUTH_ORIGINAL = 'a=%s&b=test&k=%s&e=%s&t=%s&r=%s&f=%s'
    APPID = '1252954035'
    SECRET_ID = 'AKIDrdEeu1a0lLwNcfuN8h4SeigV9brygIEz'
    SECRET_KEY = 'ra8UefW1OahrpbCbopdJo8IG4hASaYUH'
    PROFILE='dev'

class TestConfig(Config):
    DATABASE_URI = 'mysql://dementor:Messi%4010@127.0.0.1:3306/michelangelo?charset=utf8'
    LOG_FILE = '/Users/dementor/Documents/logs/xmarketing/website.log'
    CRON_LOG_FILE = '/Users/dementor/Documents/logs/xmarketing/cron.log'
    PROFILE='test'
