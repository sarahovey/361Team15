#CS 361 Group 15
#Lyft but for truck drivers


import mysql.connector
from flask import Flask, render_template, request
#app = Flask(__name__, static_folder='static')
from app import app

from flask import Flask, render_template

from app import app
#app = Flask(__name__, static_folder='static')


@app.route("/")
def main():
    return render_template('index.html');

@app.route("/hello/<name>")
def nameroute(name):
    return "Hello " + name
    
if __name__ == "__main__":
    #This is set for compabilitity with Cloud9
    app.run(host='0.0.0.0', port=8080, debug=True)


#app = Flask(__name__)
    
@app.route("/create_account", methods=['POST'])
def create_account():
    input_email=request.form['inputEmail']
    input_user=request.form['inputUsername']
    input_password=request.form['inputPassword']
    role=request.form['userType']
    conn = mysql.connector.connect(user='cs340_piccirim', password='1946', host='classmysql.engr.oregonstate.edu', database='cs340_piccirim')
    cur = conn.cursor()
    cur.execute('''INSERT INTO users(email, username, password, role) VALUES(%s,%s, %s, %s)''', (input_email, input_user, input_password, role))
    conn.commit()
    return render_template('index.html')