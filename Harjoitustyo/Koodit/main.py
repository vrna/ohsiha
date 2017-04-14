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
from bson.objectid import ObjectId
def mylists(list_id=None):
    #mytmp = []
    #mytmp.append("hjeep")
    if list_id is None:
        lists = mongo.db.lists
        tm = lists.find({}, {'_id': 1, 'name': 1, 'content': 1})
        return tm
    else:
        lists = mongo.db.lists
        tm = lists.find({ '_id': ObjectId(list_id) }, {'_id': 1, 'name': 1, 'content': 1, 'tracks': 1})
        print(tm[0] , file=sys.stderr)
        return tm[0]

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

@app.route('/lists/', methods=['POST', 'GET'])
@app.route('/lists/<list_id>', methods=['POST', 'GET'])
def lists(list_id=None):

    if list_id is not None:
        print("opening " + str(list_id), file=sys.stderr)

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
        if list_id is None:
            return render_template('actions.html',cont=mylists())
        else:
            return render_template('listview.html',cont=mylists(list_id))
# test url set
# https://open.spotify.com/track/6RrxpL1QOgTCtQZ5XvfVEa,https://open.spotify.com/track/69f8AOw6aMSyDkkDiA9nrg,https://open.spotify.com/track/5uDpwSGjljhIgDB1ZYdp9c
import spotipy
import spotipy.util
import json
@app.route('/track', methods=['GET','POST'])
def track():
    print('Came here at least', file=sys.stderr)
    if request.method == 'POST':

        playlist_id = request.form['playlist_id']
        urlInput = request.form['trackurl']
        urls = urlInput.split(',')

        trackIds = []
        for url in urls:
            trackIds.append( url.split('track/')[1])
        sp = spotipy.Spotify()
        results = sp.tracks(trackIds)

        tracks = []
        for track in results['tracks']:
            # i want to get artist and track
            artist = track["album"]["artists"][0]["name"]
            song = track["name"]
            trackname = artist + " - " + song
            tracks.append(trackname)
        lists = mongo.db.lists

        playlist = lists.find_one({'_id' : ObjectId(playlist_id)})
        if playlist is not None:
            for tr in tracks:
                playlist['tracks'].append(tr)
            lists.save(playlist)
            print("hmm saved something",file=sys.stderr)
        else:
            print("hu couldn't find it",file=sys.stderr)

    return render_template('listview.html',cont=mylists(playlist_id))
#import spotipy
#import spotipy.util
#import json

# CRUD
# add
# show
# edit
# delete

if __name__ == '__main__':
    app.secret_key = 'mysecret'

app.run(debug=True)
