from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
#app.config[‘UPLOAD_FOLDER’]	定义上传文件夹的路径
#app.config[‘MAX_CONTENT_PATH’]	指定要上传的文件的最大大小（以字节为单位）
app.config['UPLOAD_FOLDER'] = 'upload/'   #需先创建upload的文件夹

@app.route('/upload')
def upload_file():
   return render_template('flask文件上传.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      print('你好呀')
      f = request.files['file']
      print(f)
      #os.path.join连接路径，/upload   +   文件名
      print(secure_filename(f.filename))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))) #拼接进行保存
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run()