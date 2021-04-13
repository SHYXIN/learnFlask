from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

#@app.route('/hello')
def hello_world2():
   return 'hello world2'
app.add_url_rule('/hello', 'hello', hello_world2)

if __name__ == '__main__':

   app.run(debug = True)

