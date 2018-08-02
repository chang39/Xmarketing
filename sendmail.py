# -*- coding:utf-8 -*-
import smtplib
import email
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header
from xmarketing import app
from xmarketing.db import Visitor, Session
from xmarketing.util import Result
from apscheduler.schedulers.blocking import BlockingScheduler

def scan_and_send(limit=15):


    # 收件人地址或是地址列表，支持多个收件人，最多15个
    # rcptto = ['***', '***']
    visitors = Session.query(Visitor).filter(Visitor.is_sent == False).limit(limit).all()

    for visitor in visitors:
        # 自定义的回复地址
        # replyto = 'liuchang@epcchem.com'
        # 收件人地址或是地址列表，支持多个收件人，最多15个
        #rcptto = ['***', '***']
        # rcptto = 'liuchang@epcchem.com'
        # 构建alternative结构
        msg = MIMEMultipart()
        msg['Subject'] = Header('Thanks for visiting our booth at IFT2018!').encode()
        msg['From'] = '%s <%s>' % (Header('EPC Natural Products').encode(), 'epcnaturalproducts@epcchem.com')
        msg['To'] = visitor.email
        msg['Message-id'] = email.utils.make_msgid()
        msg['Date'] = email.utils.formatdate()

        email_content = app.config['EPCOLOR_MAIL_CONTENT']
        product_list = visitor.prefered_products.strip().split(',')
        print(product_list)
        if 'EPCalin' in product_list or 'MonkFruitevia' in product_list:
            email_content =  app.config['EPCALIN_MAIL_CONTENT']
            msg['Reply-to'] = app.config['EPCALIN_REPLYTO']
        else:
            msg['Reply-to'] = app.config['EPCOLOR_REPLYTO']
        # 构建alternative的text/plain部分
        textplain = MIMEText((email_content)%(visitor.visitor_name), 'plain')
        msg.attach(textplain)

        product_list.append('AboutEPC')
        print(product_list)
        for attachment in product_list:
            if attachment == 'Stevia Aroma':
                continue
            pdfpart = MIMEApplication(open(app.config['BROCHURE_FOLDER']+attachment.strip()+'.pdf', 'rb').read())
            pdfpart.add_header('Content-Disposition', 'attachment', filename=attachment.strip()+'.pdf')
            msg.attach(pdfpart)

        print (('Sending E-mail to %s') % (visitor.visitor_name))
        result_str = send_by_smtp(msg,visitor.email)
        result = json.loads(result_str)
        print (result['code'])
        if result['code'] == '0':
            visitor.is_sent = True
            Session.commit()


def send_by_smtp(msg, rcptto):
    # 发件人地址，通过控制台创建的发件人地址
    username = 'naturalproducts@epcchem.com'
    # 发件人密码，通过控制台创建的发件人密码
    password = 'epc123456'

    # 构建alternative的text/html部分
    # texthtml = MIMEText('自定义HTML超文本部分', _subtype='html', _charset='UTF-8')
    # msg.attach(texthtml)
    # 发送邮件
    try:
        #client = smtplib.SMTP()
        #python 2.7以上版本，若需要使用SSL，可以这样创建client
        client = smtplib.SMTP('smtp.263.net', 25)
        #SMTP普通端口为25或80
        # client.connect('smtp.qq.com', 587)
        #开启DEBUG模式
        client.starttls()
        client.set_debuglevel(0)
        client.login(username, password)
        #发件人和认证地址必须一致
        #备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
        #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
        client.sendmail(username, rcptto, msg.as_string())
        client.quit()
        print ('邮件发送成功！')
        return json.dumps(Result().success().set_message('success').to_dict())
    except smtplib.SMTPConnectError as e:
        return json.dumps(Result().fail().set_message('邮件发送失败，连接失败:'+e.smtp_code+e.smtp_error).to_dict())
    except smtplib.SMTPAuthenticationError as e:
        return json.dumps(Result().fail().set_message('邮件发送失败，认证错误:'+e.smtp_code+e.smtp_error).to_dict())
    except smtplib.SMTPSenderRefused as e:
        return json.dumps(Result().fail().set_message('邮件发送失败，发件人被拒绝:'+e.smtp_code+e.smtp_error).to_dict())
    except smtplib.SMTPRecipientsRefused as e:
        return json.dumps(Result().fail().set_message('邮件发送失败，收件人被拒绝:'+e.smtp_code+e.smtp_error).to_dict())
    except smtplib.SMTPDataError as e:
        return json.dumps(Result().fail().set_message('邮件发送失败，数据接收拒绝:'+e.smtp_code+e.smtp_error).to_dict())
    except smtplib.SMTPException as e:
        return json.dumps(Result().fail().set_message('邮件发送失败, '+ e.smtp_code+e.smtp_error).to_dict())
    except Exception as e:
        return json.dumps(Result().fail().set_message('邮件发送异常, '+str(e)).to_dict())

#scheduler
scheduler = BlockingScheduler()

@scheduler .scheduled_job('interval', minutes=30)
def send_job():
  scan_and_send()

if __name__ == "__main__":
  scheduler.start()
