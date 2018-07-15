# -*- coding: utf-8 -*-
import datetime
import os
import hashlib
import hmac
import base64
import ocr
from flask import Blueprint, request, redirect, url_for, render_template
from xmarketing.db import Session, Visitor
from xmarketing.util import Result
from xmarketing import app
from simplecrypt import encrypt
import logging, json
# import sendmail

mod = Blueprint('general', __name__)
logger = logging.getLogger('xmarketing')


@mod.route('/visitor-record', methods=['GET', 'POST'])
def visitor_record():
    args = request.args if request.method == 'GET' else request.form

    new_visitor = Visitor(visitor_name = args.get('visitor_name'),
                          company_name = args.get('company_name'),
                          title = args.get('title'),
                          email = args.get('email'),
                          website = args.get('website'),
                          address = args.get('address'),
                          telephone = args.get('telephone'),
                          mobile = args.get('mobile'),
                          application = args.get('application'),
                          prefered_products = args.get('product'),
                          preference = args.get('preference'),
                          create_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                          )

    Session.add(new_visitor)
    Session.commit()

    sendmail.send(app.config)

    print(json.dumps(Result().success().set_message('success').to_dict()))
    return json.dumps(Result().success().set_message('success').to_dict())

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
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

            busicard_uri += filename

            busicard_uri = 'http://p3atcmc03.bkt.clouddn.com/namecard1.jpg'

            recv_str = ocr.businesscard_recognize(app.config['APPID'], busicard_uri)
            recv_json = json.loads(recv_str)

            print(recv_str)

            if recv_json['result_list'][0]['code'] != 0:
                return 'Sorry, recognition failed...'
            recv_data = data_retrv(recv_json, filename)

            return render_template('client-info.html', data = recv_data)

    return render_template('index.html')


@app.route('/')

def data_retrv(recv_json, filename):
    result = {'filename':filename}
    data = recv_json['result_list'][0]['data']
    for attr in data:
        if ('姓名' in attr['item']) and ('visitor_name' not in result):
            result['visitor_name'] = attr['value']
            continue
        if '职位' in attr['item'] and 'title' not in result:
            result['title'] = attr['value']
            continue
        if '公司' in attr['item'] and 'company_name' not in result:
            result['company_name'] = attr['value']
            continue
        if '地址' in attr['item'] and 'address' not in result:
            result['address'] = attr['value']
            continue
        if attr['item'] == '邮箱' and 'email' not in result:
            result['email'] = attr['value']
            continue
        if attr['item'] == '网址' and 'website' not in result:
            result['website'] = attr['value']
            continue
        if attr['item'] == '电话' and 'telephone' not in result:
            result['telephone'] = attr['value']
            continue
        if attr['item'] == '手机' and 'mobile' not in result:
            result['mobile'] = attr['value']
            continue

    print (result)
    return result

def recognition(pic_uri):
    return ocr.businesscard_recognize(app.config['APPID'], pic_uri)
