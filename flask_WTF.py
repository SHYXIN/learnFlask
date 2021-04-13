
# 下面给出了Flask应用程序脚本（formexample.py）

from flask import Flask, render_template, request, flash
from forms import ContactForm       #自定义表单类
app = Flask(__name__)
#app.secret_key = 'development key'
app.secret_key = 'random string'
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   
   if request.method == 'POST':
      if form.validate() == False:   #表单验证未通过
         flash('All fields are required.\n')
         return render_template('flask_WTF.html',form = form)
      else:   ##表单验证通过
         return render_template('flask_WTF_success.html')
   #首次输入地址get访问
   elif request.method == 'GET':
         return render_template('flask_WTF.html',form = form)

if __name__ == '__main__':
   app.run(debug = True)
