from flask import Flask ,redirect, url_for, request,render_template
from firebase import firebase
import datetime
import changetime

app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://anres-test.firebaseio.com/', None)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/auth',methods = ["GET","POST"])
def auth():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['pass']
        all_user = firebase.get('users/',None)
        if username in list(all_user.keys()):
            if all_user[username] == password:
                return redirect(url_for('home',name = username))
            else:
                return redirect(url_for('error'))
    else:
        username = request.form['username']
        password = request.form['pass']
        all_user = firebase.get('users/',None)
        if username in list(all_user.keys()):
            if all_user[username] == password:
                return redirect(url_for('home',name = username))
            else:
                return redirect(url_for('error'))

@app.route('/report/<name>')
def home(name):
    return render_template("index.html",username = name)
    
@app.route('/success/<name>')
def success(name):
   return 'Thank you for helping us, %s' % name

@app.route('/submit/<name>',methods = ["GET","POST"])
def submit(name):
    if request.method == "POST":
        user = name
        way = request.form['tc']
        case = request.form['case']
        time_t = str(datetime.datetime.now())
        time = changetime.changetime(time_t)
        other = request.form['other']
        img = request.form['image']
        idd = request.form['id']
        address = '/reports/'+user+'/'+way+'/'+case+'/'+time
        firebase.put(address,name="OTHER",data=other)
        firebase.put(address,name="IMAGE",data=img)
        firebase.put(address,name="ID",data=idd)
        return redirect(url_for('success',name = user))
    else:
        return redirect(url_for('sucess',name = user))

@app.route('/error')
def error():
    return render_template("wrong_pass.html")

if __name__ == '__main__':
   app.run(debug = True)