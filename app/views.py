#CS 361 Group 15
#Lyft but for truck drivers

import mysql.connector
from flask import Flask, render_template
#app = Flask(__name__, static_folder='static')
from app import app
@app.route("/")
def main():
    return render_template('index.html');

@app.route("/hello/<name>")
def nameroute(name):
    return "Hello " + name
    
if __name__ == "__main__":
    #This is set for compabilitity with Cloud9
    app.run(host='0.0.0.0', port=8080, debug=True)

    
@app.route("/create_account")
def create_account():
    conn = mysql.connector.connect(user='cs340_piccirim', password='1946', host='classmysql.engr.oregonstate.edu', database='cs340_piccirim')
    cur = conn.cursor()
    cur.execute('''INSERT INTO users(email, username, password, role) VALUES(%s,%s, %s, %s)''', (inputEmail, inputUsername, inputPassword, role))
    conn.commit()
