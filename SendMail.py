import smtplib
import email.mime.multipart
import email.mime.text
import pickle
def Sendmail(src,dest):
    f = open('config.ini','rb')
    data = pickle.dump(f)
    f.close()
    mail = data['mail']
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = mail
    msg['to'] = mail
    msg['subject'] = 'Warning'
    content = '''''

            %s match %s
    '''%(src,dest)
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', 25)
    smtp.login(mail, 'wang3157')
    smtp.sendmail(mail, [mail],msg.as_string())
    smtp.quit()