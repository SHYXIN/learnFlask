# 参考https://blog.csdn.net/qq_28388339/article/details/87898940
from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = '847854712@qq.com'
app.config['MAIL_PASSWORD'] = 'czwucmeiwixibcag'  #'填授权码'
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = '847854712@qq.com', recipients = ['most0610@163.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   msg.html = "<b>testing</b>"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
