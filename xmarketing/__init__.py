# -*- coding: UTF-8 -*-
import os
from flask import Flask

app = Flask(__name__)
profile = os.environ.get("Xmarketing_profile",'')
app.secret_key = 'linghuchong'
app.config.from_object('config.'+profile+'Config')

from xmarketing.db import Session
from xmarketing.views import general

@app.teardown_request
def remove_db_session(exception):
    Session.remove()

import logging
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler

def init_logger():
    logger = logging.getLogger('Xmarketing')
    handler = TimedRotatingFileHandler(app.config['LOG_FILE'], when="midnight")
    handler.suffix = '%Y-%m-%d'
    handler.setFormatter(Formatter(
    '%(asctime)s %(module)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

init_logger()
app.logger.info('Xmarketing is using profile: [{0}]'.format(app.config['PROFILE']))

app.register_blueprint(general.mod)
