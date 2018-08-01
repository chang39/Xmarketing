class Config(object):
    PROJECT_NAME = 'michelangelo'
    PROFILE='default'

class DevConfig(Config):
    # Database - Url config
    DATABASE_URI = 'mysql://dementor:Messi#10@127.0.0.1:3306/epc_test?charset=utf8'
    # Img
    UPLOAD_FOLDER = '/Users/dementor/Documents/upload/xmarketing/'
    OPTIMIZE_FOLDER = '/Users/dementor/Documents/upload/xmarketing/optimize/'
    ALLOWED_EXTENSIONS = set(['jpg','jpeg'])
    # XFAPI
    APPID = '5b61658b'
    API_KEY = 'f13727bda0a563054006bf2a9dd2de35'
    # EMAIL
    EPCOLOR_MAIL_CONTENT = 'Dear %s,\n\nGreetings!\n\nMany thanks for your visiting our booth in IFT2018. Enclosed please find our brochure and flyers for EPColor. All our products are extracted from vetetables and fruits, belonged to GRAS in USA and coloring foods in Europe.\n\nFor further supports, please free to let me know. \n\n\nSonia Song\nE-mail:songwenwen@epcchem.com\nTel: 0086 10 56865512;008613581974002\n\nWish to hear more your inquires.\nHave a nice day!\nSincerely Yours,\nSonia Song'
    EPCALIN_MAIL_CONTENT = 'Dear %s,\n\nWe, EPC Natural Products C o., Ltd highly appreciated your visiting at our booth during IFT Chicago. We are honored to introduce our flavor modulating technology based on our natural ingredients EPCalin and Monk Fruitevia.\n\nWe are very proud that EPCalin and Monk Frutievia can greatly improve the overall taste in your diet applications.\n\nFor more details, please kindly see enclosed products sheets and company introduction.\n\nIf you need samples and product data sheet, please do not hesitate to contact Jay. Helsing by shixin@epcchem.com and Avril Yu by yuxiaoai@epcchem.com.\n\nAgain, we appreciate your stopped by.\n\nWith best regards,\n\nEPC Natural Products Co., Ltd\nX-Marketing'
    EPCOLOR_REPLYTO = 'songwenwen@epcchem.com'
    EPCALIN_REPLYTO = 'shixin@epcchem.com'
    BROCHURE_FOLDER = '/Users/dementor/Documents/upload/brochure/'
    EMAIL_LOG_FILE = '/Users/dementor/Documents/logs/xmarketing/email_dev.log'
    # LOG Config
    LOG_FILE = '/Users/dementor/Documents/logs/xmarketing/xmarketing_dev.log'
    PROFILE='dev'

class TestConfig(Config):
    # Database - Url config
    DATABASE_URI = 'mysql://epctest:Messi#10@127.0.0.1:3306/epc_test?charset=utf8'
    # Img
    UPLOAD_FOLDER = '/data/app/busicard/'
    OPTIMIZE_FOLDER = '/data/app/busicard/optimize/'
    ALLOWED_EXTENSIONS = set(['jpg','jpeg'])
    # XFAPI
    APPID = '5b61658b'
    API_KEY = 'f13727bda0a563054006bf2a9dd2de35'
    # EMAIL
    EPCOLOR_MAIL_CONTENT = 'Dear %s,\n\nGreetings!\n\nMany thanks for your visiting our booth in IFT2018. Enclosed please find our brochure and flyers for EPColor. All our products are extracted from vetetables and fruits, belonged to GRAS in USA and coloring foods in Europe.\n\nFor further supports, please free to let me know. \n\n\nSonia Song\nE-mail:songwenwen@epcchem.com\nTel: 0086 10 56865512;008613581974002\n\nWish to hear more your inquires.\nHave a nice day!\nSincerely Yours,\nSonia Song'
    EPCALIN_MAIL_CONTENT = 'Dear %s,\n\nWe, EPC Natural Products C o., Ltd highly appreciated your visiting at our booth during IFT Chicago. We are honored to introduce our flavor modulating technology based on our natural ingredients EPCalin and Monk Fruitevia.\n\nWe are very proud that EPCalin and Monk Frutievia can greatly improve the overall taste in your diet applications.\n\nFor more details, please kindly see enclosed products sheets and company introduction.\n\nIf you need samples and product data sheet, please do not hesitate to contact Jay. Helsing by shixin@epcchem.com and Avril Yu by yuxiaoai@epcchem.com.\n\nAgain, we appreciate your stopped by.\n\nWith best regards,\n\nEPC Natural Products Co., Ltd\nX-Marketing'
    EPCOLOR_REPLYTO = 'songwenwen@epcchem.com'
    EPCALIN_REPLYTO = 'shixin@epcchem.com'
    BROCHURE_FOLDER = '/data/app/brochure/'
    EMAIL_LOG_FILE = '/data/logs/Xmarketing/email_test.log'
    # LOG Config
    LOG_FILE = '/data/logs/Xmarketing/xmarketing_test.log'
    PROFILE='test'
