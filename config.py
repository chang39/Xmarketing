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
    EPCOLOR_MAIL_CONTENT = 'Dear %s,\n\nGreetings!\n\nMany thanks for your visiting our booth in IFT2018. Enclosed please find our brochure and flyers for EPColor. All our products are extracted from vetetables and fruits, belonged to GRAS in USA and coloring foods in Europe.\n\nFor further supports, please free to let me know. \n\n\nSonia Song\nE-mail:songwenwen@epcchem.com\nTel: 0086 10 56865512;008613581974002\n\nWish to hear more your inquires.\nHave a nice day!\nSincerely Yours,\nSonia Song'
    EPCALIN_MAIL_CONTENT = 'Dear %s,\n\nWe, EPC Natural Products C o., Ltd highly appreciated your visiting at our booth during IFT Chicago. We are honored to introduce our flavor modulating technology based on our natural ingredients EPCalin and Monk Fruitevia.\n\nWe are very proud that EPCalin and Monk Frutievia can greatly improve the overall taste in your diet applications.\n\nFor more details, please kindly see enclosed products sheets and company introduction.\n\nIf you need samples and product data sheet, please do not hesitate to contact Jay. Helsing by shixin@epcchem.com and Avril Yu by yuxiaoai@epcchem.com.\n\nAgain, we appreciate your stopped by.\n\nWith best regards,\n\nEPC Natural Products Co., Ltd\nX-Marketing'
    EPCOLOR_REPLYTO = 'songwenwen@epcchem.com'
    EPCALIN_REPLYTO = 'shixin@epcchem.com'
    BROCHURE_FOLDER = '/Users/dementor/Documents/upload/brochure/'

class TestConfig(Config):
    DATABASE_URI = 'mysql://epctest:Messi#10@127.0.0.1:3306/epc_test?charset=utf8'
    UPLOAD_FOLDER = '/data/app/busicard/'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
    PIC_URL = 'http://123.206.55.228/busicard/'
    AUTH_ORIGINAL = 'a=%s&b=test&k=%s&e=%s&t=%s&r=%s&f=%s'
    APPID = '1252954035'
    SECRET_ID = 'AKIDrdEeu1a0lLwNcfuN8h4SeigV9brygIEz'
    SECRET_KEY = 'ra8UefW1OahrpbCbopdJo8IG4hASaYUH'
    PROFILE='test'
    EPCOLOR_MAIL_CONTENT = 'Dear %s,\n\nGreetings!\n\nMany thanks for your visiting our booth in IFT2018. Enclosed please find our brochure and flyers for EPColor. All our products are extracted from vetetables and fruits, belonged to GRAS in USA and coloring foods in Europe.\n\nFor further supports, please free to let me know. \n\n\nSonia Song\nE-mail:songwenwen@epcchem.com\nTel: 0086 10 56865512;008613581974002\n\nWish to hear more your inquires.\nHave a nice day!\nSincerely Yours,\nSonia Song'
    EPCALIN_MAIL_CONTENT = 'Dear %s,\n\nWe, EPC Natural Products C o., Ltd highly appreciated your visiting at our booth during IFT Chicago. We are honored to introduce our flavor modulating technology based on our natural ingredients EPCalin and Monk Fruitevia.\n\nWe are very proud that EPCalin and Monk Frutievia can greatly improve the overall taste in your diet applications.\n\nFor more details, please kindly see enclosed products sheets and company introduction.\n\nIf you need samples and product data sheet, please do not hesitate to contact Jay. Helsing by shixin@epcchem.com and Avril Yu by yuxiaoai@epcchem.com.\n\nAgain, we appreciate your stopped by.\n\nWith best regards,\n\nEPC Natural Products Co., Ltd\nX-Marketing'
    EPCOLOR_REPLYTO = 'songwenwen@epcchem.com'
    EPCALIN_REPLYTO = 'shixin@epcchem.com'
    BROCHURE_FOLDER = '/data/app/brochure/'
