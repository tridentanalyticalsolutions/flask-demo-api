from flask import Blueprint
from flask_restful import Resource
from flask import redirect,request,url_for,session,abort, Response,jsonify
from pymongo import MongoClient
import bcrypt
from bson import ObjectId
mod = Blueprint('api',__name__)

# connect to db
# to be added in config file in project destructuring
client = MongoClient("mongodb://db:27017")
db = client.SentencesDatabase
usersModel = db["Users"]

@mod.route('/')
def welcome():
    return jsonify(apiResponse(200,"Apis are working successfully"))
   
@mod.route('/users',methods=["GET"])
def users():
    userList = []
    for user in usersModel.find():
        # because we don't want to send password to the user
        user.pop('Password')
        user['_id'] = str(user['_id'])
        userList.append(user)

    return jsonify(apiResponse(200,"users list fetched successfully",userList))

# register user
@mod.route('/users',methods=["POST"])

def registerUser():
    if request.data.decode() == '':
       return jsonify(apiResponse(201,"name,username,password is required"))
    
    try:
       postedData = request.get_json()
    except:
         return jsonify(apiResponse(201,"name,username,password is required"))
    
    if not 'name' in postedData.keys() or not 'username' in postedData.keys() or not 'password' in postedData.keys():
        return jsonify(apiResponse(201,"name,username,password is required"))
    
    # validate data from the input
    # later moved to validation.py file for all validations
    nameValidationResponse = validateData('name',postedData["name"])
    if  201 == nameValidationResponse.json['status']:
        return nameValidationResponse
    usernameValidationResponse = validateData('username',postedData["username"])
    if  201 == usernameValidationResponse.json['status']:
        return usernameValidationResponse
    passwordValidationResponse = validateData('password',postedData["password"])
    if  201 == passwordValidationResponse.json['status']:
        return passwordValidationResponse

    #Get the data
    name = postedData["name"]
    username = postedData["username"]
    password = postedData["password"] #"123xyz"
    hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    #Store username and pw into the database
    usersModel.insert({
        "name": name,
        "Username": username,
        "Password": hashed_pw,
        "Sentence": "",
        "Tokens":6
    })
    return jsonify(apiResponse(200,"You successfully signed up for the API"))

def validateData(key,value):
    if value == '':
        return jsonify(apiResponse(201, key  + " cannot be blank"))

    return jsonify(apiResponse(200, ''))



# to be moved in utls folder
def apiResponse(status,message,responseData=[]):
    return { 
        "status": status,
         "msg": message,
         "responseData":responseData
    }

