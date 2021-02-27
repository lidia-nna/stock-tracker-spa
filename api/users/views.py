from flask import jsonify, request, render_template
from .emailtoken import Token, Email
from . import users
from ..config import DevConfig
from ..models import UserModel, Tickers
from flask_jwt_extended import (create_access_token, 
create_refresh_token,
set_refresh_cookies, 
set_access_cookies, 
jwt_required, 
get_jwt_identity, 
unset_jwt_cookies)
import datetime


@users.route('/auth', methods=["POST"])
def login():
    if not request.form:
        return "Invalid format", 400
    data = request.form
    current_user = UserModel.check_user(username=data.get('username'))
    if not current_user:
        return 'Username not found', 401
    if not UserModel.is_password(current_user.passwd_hash, data.get('password')):
        return 'Wrong credentials', 401
    if not current_user.confirmed:
        return "Unconfirmed account", 403
    access_token = create_access_token(identity=current_user.id)
    refresh_token = create_refresh_token(identity=current_user.id)
    # resp = make_response(redirect(f'/home/{current_user.id}'))
    resp = {
            'user': current_user.id,
            'access_token' : access_token,
            'refresh_token': refresh_token
        }
    
    #set_refresh_cookies(resp, refresh_token)
    #set_access_cookies(resp, access_token)
    return jsonify(resp), 200

@users.route('/register', endpoint='register', methods=["POST"])
def register(): 
    if not request.form:
        print (request.data)
        return "Invalid format", 400
    data = request.form
    user = UserModel.check_user(username=data.get('username')) 
    if user and user.confirmed:
        print(user)
        return "Already registered", 409
    elif user and not user.confirmed:
        return "Unconfirmed account", 403     
    if UserModel.check_user(username=data.get('username')):
        return {'message': 'this username already exists, please select a different name'}
    token = Token()
    mytoken = token.generate_confirmation_token(email=data.get('email'))
    confemail = Email()
    confirm_url= f'http://127.0.0.1:5000/confirmreg/{mytoken}'
    try:
        r = confemail.send_email(
            subject="NoReply: Stock Tracker account registration", 
            to=data.get('email'), 
            template=render_template("email_template.html", confirm_url=confirm_url))
        print('Email sent?:', r)
    except Exception as e:
        print(e)
        return "Fail", 500
    else:
        user = UserModel(email=data.get('email'), username=data.get('username'))
        user.set_password(data.get('password'))
        # user.set_username()
        try:
            user.save_to_db()
        except Exception as e:
            return {'message': f'Something went wrong: {e}'}, 400
        else: 
            return "User registered", 200


# update password or email       
def put():
    pass

#remove the profile TEST!!!
def delete():
    user = get_jwt_identity()
    #find records in db
    user_record = UserModel.find_user_record(user_id=user)
    # ticker_records = Tickers.find_all_tickers(user_id=user)
    try:
        user_record.delete()
        return "Success", 200
    except Exception as e:
        print('Failed to remove the user record' +str(e))
        return "Removal unsuccessful", 500

@users.route('/unconfirmed', methods=["POST"])
def unconfirmed_registration():
    if not request.is_json:
        return "Invalid format", 400
    data = request.get_json()
    print(data)
    user = UserModel.check_user(email=data.get('email')) 
    if user and not user.confirmed:
        token = Token()
        mytoken = token.generate_confirmation_token(user.email)
        confemail = Email()
        confirm_url= f'http://127.0.0.1:5000/confirmreg/{mytoken}'
        confemail.send_email(
            subject="Travelmap account registration", 
            to=user.email, 
            template=render_template("email_template.html", confirm_url=confirm_url)
            )
        return "Confirmation sent", 200
    return "Account not found", 401
            

@users.route('/confirmreg/<token>')
def confirm_registration(token):
    # if not request.args:
    #     return "Missing token", 400
    # token = request.args.get('token')
    tokenclass = Token()
    email = tokenclass.confirm_token(token)
    if not email:
        return "Invalid or expired token", 400
    user = UserModel.check_user(email=email)   
    if not user.confirmed:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        user.save_to_db()
        return "Account confirmed", 201
    return "Already confirmed", 409


        

@users.route('/token/refresh', endpoint='refresh_token', methods=["GET"])
@jwt_required(refresh=True)
def refresh_token():
    try:
        current_user = get_jwt_identity()
        print('current_user', current_user)
        access_token = create_access_token(identity=current_user)
        print('access token', access_token)
        resp = {
            'current user': current_user,
            'access_token' : access_token
        }
        #set_access_cookies(resp, access_token)
        return jsonify(resp)
    except:
        return "Refresh token expired", 401

# @jwt_required(refresh=True)
# @users.route('/token/remove', endpoint='logout', methods=["POST"])
# def logout():
#     resp = jsonify({'logout': True})
#     unset_jwt_cookies(resp)
#     resp.set_cookie('refresh_token_cookie', expires=0)
#     resp.set_cookie('csrf_refresh_token', expires=0)
#     return resp

#to_test
# class AllUsers(Resource): 
#     def get():
#         def to_json(x):
#             return {
#                 'username': x.username,
#                 'email': x.email,
#                 'password': x.passwd_hash
#             }
#         return [to_json(user) for user in UserModel.query.all()]

#     def delete():
#         return UserModel.delete_all()

# #to_test
# class SecretResource(Resource):
#     @jwt_required
#     def get():
#         return {
#             'answer': 42,
#             'current user': get_jwt_identity()
#         }
