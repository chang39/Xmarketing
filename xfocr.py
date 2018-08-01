import requests
import time
import json, logging
import hashlib
import base64
from urllib.parse import urlencode, quote_plus
from xmarketing import app

logger = logging.getLogger('Xmarketing')

def businesscard_recognize(file):
    # open img file
    f = open(file, 'rb')
    file_content = f.read()

    # make http body
    base64_image = base64.b64encode(file_content)
    body = urlencode({'image': base64_image} , quote_via=quote_plus)
    app.logger.info('Body: Image file has been encoded by Base64..')

    # header preparetion
    api_key = app.config['API_KEY']
    param = {"engine_type": "business_card"}

    x_appid = app.config['APPID']
    x_param = base64.standard_b64encode(json.dumps(param).encode('UTF-8'))
    app.logger.info('Header: Base64 x_param [{0}]'.format(x_param.decode('UTF-8')))
    x_time = int(int(round(time.time() * 1000)) / 1000)
    # header authorization signature
    x_checksum = hashlib.md5((api_key + str(x_time) + x_param.decode('UTF-8')).encode('UTF-8')).hexdigest()
    app.logger.info('Header: MD5 x_checksum [{0}]'.format(x_checksum))
    # make http header
    x_header = {'X-Appid': x_appid,
                'X-CurTime': str(x_time),
                'X-Param': x_param.decode('UTF-8'),
                'X-CheckSum': x_checksum,
                'Content-Type':'application/x-www-form-urlencoded'}

    url = 'http://webapi.xfyun.cn/v1/service/v1/ocr/business_card'
    res = requests.post(url, data=body,headers=x_header)
    app.logger.info('XF Recognition Succeed!')

    return res.json()
