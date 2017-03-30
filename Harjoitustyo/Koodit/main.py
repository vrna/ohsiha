from __future__ import print_function
from flask import Flask, render_template, url_for, request, session, redirect
import pymongo
from flask_pymongo import PyMongo
import bcrypt
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
collection = db.test_collection
#client.drop_database("test_database")
app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'test_collection'
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/'

mongo = PyMongo(app)
mytmp = []
def mylists():
    #mytmp = []
    #mytmp.append("hjeep")
    lists = mongo.db.lists
    tm = lists.find({}, {'_id': 0, 'name': 1, 'content': 1})
    return tm
    #lists = mongo.db.lists
    #mytmp2= list()
    #for lis in lists.find():
    #    print (lis)
    #    mytmp2.append(lis)
    #mytmp = mytmp2

@app.route('/')
def index():
    if 'username' in session:
        mytmp = mylists()
        return render_template("actions.html",cont=mytmp)
        #return 'You are logged in as ' + session['username']

    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'

import sys
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        #print('Hello world!', file=sys.stderr)
        if request.form['username'] == "" or request.form['pass'] == "":
            return "please set an username"

        if existing_user is None:

            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('register.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/list', methods=['POST', 'GET'])
def list():
    if request.method == 'POST':
        print('post' , file=sys.stderr)
        if request.form['listname'] == "":
            print("empty list name ", file=sys.stderr)
            return render_template('actions.html',cont=mylists())

        print('Posting ' + request.form['listname'] , file=sys.stderr)
        lists = mongo.db.lists


        existing = lists.find_one({'name' : request.form['listname']})
        if existing is None:
            
            lists.insert({'name' : request.form['listname'], 'content' : request.form['content']})
            print("it doesn't exist..", file=sys.stderr)
        else:
            print("it exists", file=sys.stderr)

            if request.form.get('deleting') is not None:
                print("we should be deleting",file=sys.stderr)
                lists.delete_one(existing)
            else:
                print(existing)
                existing['content'] = request.form['content']
                lists.save(existing)
            #lists.update({'_id':existing._id}, {"$set": request.form['content']}, upsert=False)

        return render_template('actions.html',cont=mylists())
    if request.method == 'GET':
        print('Getting!', file=sys.stderr)
        #ls = mylists()
        #return render_template('actions.html',cont=ls)
        return render_template('actions.html',cont=mylists())

# CRUD
# add
# show
# edit
# delete

if __name__ == '__main__':
    app.secret_key = 'mysecret'

app.run(debug=True)
