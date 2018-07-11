# -*- coding: utf-8 -*-
import datetime
import os
import hashlib
import hmac
import base64
import ocr
from flask import Blueprint, request, redirect, url_for
from xmarketing.db import Session, Visitor
from xmarketing.util import Result
from xmarketing import app
from simplecrypt import encrypt
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

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/uploadorscan', methods=['GET', 'POST'])
def upload_file():
    busicard_uri = app.config['PIC_URL']
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'.'+file.filename.rsplit('.', 1)[1].lower()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('upload_file',filename=filename))
            busicard_uri += filename
            print('======' + busicard_uri + '======')
            busicard_uri = 'http://p3atcmc03.bkt.clouddn.com/namecard1.jpg'
            rec_str = ocr.businesscard_recognize(app.config['APPID'], busicard_uri)

    return rec_str

def recognition(pic_uri):
    return ocr.businesscard_recognize(app.config['APPID'], pic_uri)


@mod.route('/test', methods=['GET'])
def test():
    return "Hello!"
