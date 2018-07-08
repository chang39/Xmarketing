# -*- coding: UTF-8 -*-

import os
from flask import Flask

app = Flask(__name__)
profile = os.environ.get("Xmarketing_profile",'')
app.config.from_object('config.'+profile+'Config')

from xmarketing.db import Session
from xmarketing.views import general

@app.teardown_request
def remove_db_session(exception):
    Session.remove()

app.register_blueprint(general.mod)
