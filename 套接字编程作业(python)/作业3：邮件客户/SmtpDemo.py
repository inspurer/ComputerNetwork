#作业3：邮件客户
from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

mail_server = 'smtp.163.com'
#根据发送方邮箱确定邮箱服务器
#qq邮箱的服务器为smtp.qq.com;163邮箱为smtp.163.com
def get_mail_server(sender):
    key = sender[sender.index('@')+1:]
    return "smtp."+key

port = '25'  ## SMTP协议默认端口是25
sender = '2391527690@qq.com'
mail_server = get_mail_server(sender)
sender_pass = 'creivoxgdidgdijb'    #注意是授权码,而不是登录密码,需要在邮箱端先获取
#我的163邮箱授权码为：XT9527;qq邮箱为：creivoxgdidgdijb
receiver = 'csu_xiaotao@163.com'
mail_msg = 'this is a demo'

#第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText(mail_msg, 'plain', 'utf-8')
msg['From'] = sender
msg['To'] = receiver
#Header对象编码文本，包含utf-8编码信息和Base64编码。
msg['Subject'] = Header('来自inspurer的个人计算机', 'utf-8')
try:
    server = SMTP(mail_server, port)
    #用set_debuglevel(1),可以打印出和SMTP服务器交互的所有信息
    #server.set_debuglevel(1)
    server.login(sender, sender_pass)
    #由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
    server.sendmail(sender, (receiver), msg.as_string() )
    server.quit()
    print("邮件发送成功！")
except:
    server.quit()
    print("邮件发送失败！")

#更多扩展参见：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000#0