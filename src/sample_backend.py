from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
import random
import string


app = Flask(__name__)
CORS(app)

@app.route('/')

def hello_world():
    return 'Hello, World!'
    
users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'bjk123', 
         'name': 'Susie',
         'job': 'Doctor',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      elif search_username  :
         return find_users_by_name(search_username)  
      elif search_job  :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = generateID()
      users['users_list'].append(userToAdd)
      resp = jsonify(name = userToAdd['name'],
      job = userToAdd['job'], id = userToAdd['id'], 
      success=True)
      resp.status_code = 201
      return resp
   
@app.route('/users/<id>', methods=['GET', 'DELETE'])

def get_user(id):
   if request.method == 'GET':
      if id :
         for user in users['users_list']:
            if user['id'] == id:
               return user
            return ({})
      return users
   elif request.method == 'DELETE':
      for user in users['users_list']:
         if user['id'] == id:
            users['users_list'].remove(user)
            resp = jsonify(success=True)
            resp.status_code = 204
            return resp
      resp = jsonify(success=False)
      resp.status_code = 404
      return resp
   
def find_users_by_name(name):
   subdict = {'users_list' : []}
   for user in users['users_list']:
      if user['name'] == name:
         subdict['users_list'].append(user)
   return subdict

def generateID():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))