import QcloudAuthSign
import requests
import urllib
import json

ocr_host = "recognition.image.myqcloud.com"
ocr_request_url = "http://recognition.image.myqcloud.com/ocr/businesscard"

def businesscard_recognize(appid, pic_uri):
    params = {'appid': appid, 'url_list': pic_uri}
    headers = {"host": ocr_host, "content-type": "application/json", "authorization": QcloudAuthSign.getSignature()}
    res = requests.post(ocr_request_url, data = json.dumps(params),headers = headers)
    return res.text
