import hashlib
import hmac
import base64
import time
import random
import datetime
from xmarketing import app

def make_digest(message, key):

    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')

    digester = hmac.new(key, message, hashlib.sha1)
    signature1 = digester.digest()
    print(signature1)

    signature2 = base64.standard_b64encode(signature1+message)
    print(signature2)

    return str(signature2, 'UTF-8')

def getSignature():

    today = datetime.datetime.now()
    expire = today + datetime.timedelta(minutes = 10)

    timestamp = str(int(time.mktime(today.timetuple())))
    timestampex = str(int(time.mktime(expire.timetuple())))

    rand = str(random.randint(0,999999999))
    fileid = ''

    original = app.config['AUTH_ORIGINAL'] % (app.config['APPID'],app.config['SECRET_ID'], timestampex, timestamp, rand, fileid)
    print(original)
    return make_digest(original, app.config['SECRET_KEY'])

if __name__ == "__main__":
    print(getSignature())
