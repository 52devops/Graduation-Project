import smtplib
import email.mime.multipart
import email.mime.text
import pickle
def Sendmail(src=1,dest=1):
    f = open('config.ini','rb')
    data = pickle.load(f)
    f.close()
    mail = data['mail']
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = mail
    msg['to'] = mail
    msg['subject'] = 'Warning'
    content = '''''

            %s样本图片与刚刚抓取的%s图像匹配，请注意。
    '''%(src,dest)
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', 25)
    smtp.login(mail, 'wang3157')
    smtp.sendmail(mail, [mail],msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    Sendmail()