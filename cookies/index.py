from flask import *
app = Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('read_cookie.html'))
        resp.set_cookie('userID', user)
        return resp
    else:
        return "<h1>Brijesh</h1>"

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'

if __name__ == '__main__':
   app.run(debug = True)
