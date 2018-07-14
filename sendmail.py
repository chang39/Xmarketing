# -*- coding:utf-8 -*-
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header
from xmarketing import app


def send(replyto, rcptto, email_content, attachments):
    # 发件人地址，通过控制台创建的发件人地址
    username = 'naturalproducts@epcchem.com'
    # 发件人密码，通过控制台创建的发件人密码
    password = 'epc123456'
    # 自定义的回复地址
    #replyto = '441756412@qq.com'
    # 收件人地址或是地址列表，支持多个收件人，最多30个
    #rcptto = ['***', '***']
    #rcptto = '441756412@qq.com'
    # 构建alternative结构
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header('Thanks for visiting our booth at IFT2018!'.decode('utf-8')).encode()
    msg['From'] = '%s <%s>' % (Header('EPC Natural Products'.decode('utf-8')).encode(), username)
    msg['To'] = rcptto
    msg['Reply-to'] = replyto
    msg['Message-id'] = email.utils.make_msgid()
    msg['Date'] = email.utils.formatdate()

    # 构建alternative的text/plain部分
    textplain = MIMEText(email_content, _subtype='plain', _charset='UTF-8')
    msg.attach(textplain)

    # msg.attach(MIMEText(file("/Users/dementor/Downloads/lipstick.pdf").read()))
    # msg.attach(MIMEText(file("/Users/dementor/Downloads/EPC Company.pdf").read()))
    for attachment in attachments:
        pdfpart = MIMEApplication(open(app.config['BROCHURE_FOLDER']+attachment+'.pdf', 'rb').read())
        pdfpart.add_header('Content-Disposition', 'attachment', filename=attachment+'.pdf')
        msg.attach(pdfpart)

    # 构建alternative的text/html部分
    # texthtml = MIMEText('自定义HTML超文本部分', _subtype='html', _charset='UTF-8')
    # msg.attach(texthtml)
    # 发送邮件
    try:
        #client = smtplib.SMTP()
        #python 2.7以上版本，若需要使用SSL，可以这样创建client
        client = smtplib.SMTP_SSL()
        #SMTP普通端口为25或80
        client.connect('smtp.263.net', 465)
        #开启DEBUG模式
        client.set_debuglevel(0)
        client.login(username, password)
        #发件人和认证地址必须一致
        #备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
        #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
        client.sendmail(username, rcptto, msg.as_string())
        client.quit()
        print '邮件发送成功！'
    except smtplib.SMTPConnectError, e:
        print '邮件发送失败，连接失败:', e.smtp_code, e.smtp_error
    except smtplib.SMTPAuthenticationError, e:
        print '邮件发送失败，认证错误:', e.smtp_code, e.smtp_error
    except smtplib.SMTPSenderRefused, e:
        print '邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error
    except smtplib.SMTPRecipientsRefused, e:
        print '邮件发送失败，收件人被拒绝:', e.smtp_code, e.smtp_error
    except smtplib.SMTPDataError, e:
        print '邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error
    except smtplib.SMTPException, e:
        print '邮件发送失败, ', e.message
    except Exception, e:
        print '邮件发送异常, ', str(e)
