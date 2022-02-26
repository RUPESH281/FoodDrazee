from email import header
import imp
from urllib import response
import requests
import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/auth_details'
db = SQLAlchemy(app)
 

class Tokendetails(db.Model):
    phone_number = db.Column(db.String(11), primary_key=True)
    token_id = db.Column(db.String(10000))


@app.route('/')
def welcome():
    return f'Hello World'




@app.route('/signUpNew', methods = ['POST'])
def signUpNew():
    dict={
        "lead_id": 30,
        "goal": "Weight Loss",
        "diet": "Flexible",
        "name": "nish",
        "email": "nishil@gmai.com",
        "phone": "9821251354",
        "age": 24,
        "height_feet": 5,
        "height_inches": 8,
        "weight": 77,
        "activities": "No Physical Activity",
        "meal_preference": "Eggetarian",
        "egg_in_bread": "Yes",
        "start_date": "28/06/2021",
        "no_of_days": 30,
        "whatsapp_consent": 1,
        "body_fat": "Normal",
        "last_page": "physical-activities",
        "notes": "I want good food only",
        "dont_eat_egg_on": [
            "tue"
        ],
        "doesnt_eat_meat": [
            "mutton"
        ],
        "dont_eat_nonveg_on": [
            "thu"
        ],
        "meals": [
            "lunch"
        ],
        "addresses": {
            "is_evening_address_same": "false",
            "is_weekend_address_same": "false",
            "is_weekend_evening_address_same": "false",
            "default": {
            "street": "This is my Address",
            "street_2": "This is new Address",
            "pincode": "400050",
            "landmark": "Devi Temple",
            "city": "Mumbai",
            "state": "Maharashtra"
            },
            "evening_address": {
            "street": "This is my Address",
            "street_2": "This is new Address",
            "pincode": "400050",
            "landmark": "Devi Temple",
            "city": "Mumbai",
            "state": "Maharashtra"
            },
            "weekend_address": {
            "street": "This is my Address",
            "street_2": "This is new Address",
            "pincode": "400050",
            "landmark": "Devi Temple",
            "city": "Mumbai",
            "state": "Maharashtra"
            },
            "weekend_evening_address": {
            "street": "This is my Address",
            "street_2": "This is new Address",
            "pincode": "400050",
            "landmark": "Devi Temple",
            "city": "Mumbai",
            "state": "Maharashtra"
            }
        }
        }

    headers={
        'Content-Type': 'application/json'
        }

    url= "https://erp-test.fooddarzee.com/api/signUpNew"
    response = requests.post(url, data=json.dumps(dict), headers=headers)

    return response.json()




@app.route('/login', methods = ['POST'])
def login():
    url="https://erp-test.fooddarzee.com/api/login"
    input={
        "phone": 9920045322
    }
    header= {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(input), headers=header)
    return response.json()




@app.route('/resendOtp', methods = ['POST'])
def resendOtp():
    url="https://erp-test.fooddarzee.com/api/resendOtp"
    input={
        "phone": 9920045322
    }
    header= {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(input), headers=header)
    return response.json()




@app.route('/verifyOtp', methods = ['POST'])
def verifyOtp():
    url="https://erp-test.fooddarzee.com/api/verifyOtp"
    input={
        "phone": 9920045322,
        "otp": 9999
    }
    header= {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(input), headers=header)
    if (request.method=='POST'):
        response_data=response.json()
        phonenumber=response_data['data']['user']['phone']
        tokenid=response_data['data']['token']
        entry = Tokendetails(token_id=tokenid, phone_number=phonenumber)
        db.session.add(entry)
        db.session.commit()
    return response.json()

    
    




@app.route('/v1/address', methods= ['GET'])
def v1addressget():
    url ="https://erp-test.fooddarzee.com/api/v1/address"
    data = Tokendetails.query.filter_by(phone_number=9920045322).first()
    auth_token=data.token_id    
    header= {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }
    response = requests.get(url, headers=header)
    return response.json()




@app.route('/v1/address', methods= ['POST'])
def v1addresspost():
    url ="https://erp-test.fooddarzee.com/api/v1/address"
    data = Tokendetails.query.filter_by(phone_number=9920045322).first()
    auth_token=data.token_id 
    input={
        "label": "A nice Address",
        "street_1": "This is my Address",
        "street_2": "This is new Address",
        "pincode": "400050",
        "area": "Bandra West",
        "city": "Mumbai",
        "state": "Maharashtra"
    }
    header= {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }
    response = requests.post(url, data=json.dumps(input), headers=header)
    return response.json()



@app.route('/v1/address/<string:num>', methods=['PUT'])
def v1addressput(num):
    url = "https://erp-test.fooddarzee.com/api/v1/address/"
    base_url=url+num
    data = Tokendetails.query.filter_by(phone_number=9920045322).first()
    auth_token=data.token_id
    input={
        "label": "A nice Address",
        "street_1": "This is my Address",
        "street_2": "This is new Address",
        "pincode": "400050",
        "area": "Bandra West",
        "city": "Mumbai",
        "state": "Maharashtra"
    }
    header= {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }
    response = requests.put(url=base_url, data=json.dumps(input), headers=header)
    return response.json()



@app.route('/v1/address/<string:num>', methods=['DELETE'])
def v1addressdelete(num):
    url = "https://erp-test.fooddarzee.com/api/v1/address/"
    base_url=url+num
    data = Tokendetails.query.filter_by(phone_number=9920045322).first()
    auth_token=data.token_id
    header= {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }
    response = requests.delete(url=base_url, headers=header)
    return response.json()



@app.route('/v1/customer', methods=['GET'])
def v1customer():
    url = "https://erp-test.fooddarzee.com/api/v1/customer"
    data = Tokendetails.query.filter_by(phone_number=9920045322).first()
    auth_token=data.token_id 
    header={
        'Authorization': 'Bearer ' + auth_token,
        'accept': 'application/json'
    }
    
    response = requests.get(url, headers=header)
    return response.json()




@app.route('/v1/customer/changePhone', methods=['POST'])
def v1customerchangePhone():
    url = "https://erp-test.fooddarzee.com/api/v1/customer/changePhone"
    data = Tokendetails.query.filter_by(phone_number=9920045322).first()
    auth_token=data.token_id
    input={
        "phone": 9920045322,
        "otp": 9999
    }
    header= {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + auth_token
    }
    response = requests.post(url, data=json.dumps(input), headers=header)
    return response.json()



if __name__ == '__main__':
    app.run(debug=True)