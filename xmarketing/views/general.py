# -*- coding: utf-8 -*-
import datetime
from flask import Blueprint, request
from xmarketing.db import Session, Visitor
from xmarketing.util import Result
import logging, json

mod = Blueprint('general', __name__)
logger = logging.getLogger('xmarketing')


"""
    url
      /send-sms
    param
      phone: string; required; target phone to send sms
      content: string; required; content to send (yunpina should create the template in yupian admin platform)
      schedule_seconds: string; optional; default is 0, send immediately
    TODO
      request param validate to construct result
"""
@mod.route('/visitor-record', methods=['GET', 'POST'])
def visitor_record():
    args = request.args if request.method == 'GET' else request.form

    new_visitor = Visitor(visitor_name = args.get('visitor_name'),
                          company_name = args.get('company_name'),
                          email = args.get('email'),
                          website = args.get('website'),
                          address = args.get('address'),
                          telephone = args.get('telephone'),
                          mobile = args.get('mobile'),
                          fax = args.get('fax'),
                          preference = args.get('preference'),
                          create_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                          )

    Session.add(new_visitor)
    Session.commit()
    print(json.dumps(Result().success().set_message('success').to_dict()))
    return json.dumps(Result().success().set_message('success').to_dict())

@mod.route('/test', methods=['GET'])
def test():
    return "Hello!"
