'''

Flask application script to create the backend endpoints for the software

=================================================================================================================

Endpoints: 

1. /
empty()  --  empty function that only returns a static string


2. /items/

    Input parameters: 
    None

    Output:
    Response returns the items present in table

3. /additem/

    Input parameters:
    item_name, quantity, description, zipcode, city, donor_id, category

    Output:
    Response returns a success, message

4. /updateitem/

    Input parameters:
    item_name, quantity, description, zipcode, city, donor_id, category

    Output:
    Response returns a success, message

----------------------------------------------------------------------------------------------------------------
'''
# required imports
from werkzeug.exceptions import HTTPException
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from src.Backend.utils import *
from cryptography.fernet import Fernet
key = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(key)
import smtplib
from smtplib import SMTP
import os
import time

# Flask application configuration
app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = "src/Backend/images/"


#### error handlers ####
# http exceptions handler
# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     """Return JSON instead of HTML for HTTP errors."""
#     # start with the correct headers and status code from the error
#     response = e.get_response()
#     # replace the body with JSON
#     response.data = json.dumps({
#         "code": e.code,
#         "name": e.name,
#         "description": e.description,
#     })
#     response.content_type = "application/json"
#     logging.error('########### ' + str(e) + ' ###########', exc_info=True)
#     return response


# @app.errorhandler(Exception)
# def handle_exception(e):
#     # pass through HTTP errors
#     if isinstance(e, HTTPException):
#         return e
#     err = {
#         "code": -1,
#         "name": "Server Error",
#         "description": "Unexpected Error. Please contact Admin"

#     }
#     logging.error('########### ' + str(e) + ' ###########', exc_info=True)
#     # now you're handling non-HTTP exceptions only
#     return jsonify(err)

#### end of error handlers ####


@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def empty():
    """
    Empty function which sends a json when we start the application.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    return jsonify({"status": 200, "data": {}, "message": "Backend working"})


@app.route('/items', methods=['GET', 'OPTIONS'])
def home():
    """
    Dashboard which contains a set of items that interests the user.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    page : int
        Page number of the home dashboard for a particular user. 
    id : int
        ID of the user to get their interested items.

    Returns
    ----------
    json
        Returns a json containing the status, data which contains interested items for the user, message in accordance with the status.
    """

    if request.method == 'GET':
        page = request.args.get('page')
        id = request.args.get('id')
        print(page)
        status, msg = get_items(page, id)

        if status:
            if msg == []:
                return jsonify({"status": 200, "data": {}, "message": "No more data"})
            else:
                return jsonify({"status": 200, "data": msg, "message": "Fetched records successfully"})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/uploadimage', methods=['POST', 'GET', 'OPTIONS'])
def upload_image():
    """
    Method used to upload an image to given folder.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - The filename of the saved image.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    image : FileStorage
        The image to be uploaded to the given upload folder. 

    Returns
    ----------
    json
        Returns a json containing the status, data which contains interested items for the user, message in accordance with the status.
    """

    if request.method == 'POST':
        if not os.path.isdir(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)

        img = request.files['image']
        file_name = img.filename
        if UPLOAD_FOLDER not in file_name:
            file_name = time.strftime("%Y%m%d-%H%M%S") + '_' + file_name
            file_name = os.path.join(UPLOAD_FOLDER, file_name)
        img.save(file_name)

        return jsonify({"status": 200, "data": {"imgName": file_name}, "message": ""})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/additem', methods=['POST', 'GET', 'OPTIONS'])
def additem():
    """
    Inserting an item into the dashboard.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    data : json
        Information about item which is going to get added into the dashboard.

    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'POST':
        data = json.loads(request.data)

        status, msg = insert_item(
            data['item_name'], data['quantity'], data['description'], data['zipcode'], data['city'], data['donor_id'],
            data['category'], data['img_url'])

        if status:
            cursor = connection.cursor(dictionary=True)
            sql_get_data_query = """select email from users"""
            cursor.execute(sql_get_data_query)
            data = cursor.fetchall()
            emails = [d['email'] for d in data]
            smtp_port = SMTP("smtp.gmail.com", 587)
            try:
                smtp_port.ehlo()
                smtp_port.starttls()
                smtp_port.login('donatifynotifications@gmail.com' , 'pvuiescbegnhpxyj')
                subject = 'A new item is up for donation!!'
                body = 'A new item is up for donation. Go to Donatify app to be the first person to get the item!! Hurry up!!'
                email_text = 'Subject: {}\n\n{}'.format(subject, body)
                smtp_port.sendmail('donatifynotifications@gmail.com', emails, email_text)
                print("Email Sent")
            except Exception as ex:
                print ("Something went wrong….",ex)
            smtp_port.quit()
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/updateitem', methods=['POST', 'PUT', 'GET', 'OPTIONS'])
def updateitem():
    """
    Updating an item which is currently posted on the dashboard.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    data : json
        Updated Item information.

    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'PUT':
        data = json.loads(request.data)

        status, msg = update_item(data)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/addDonation', methods=['POST', 'GET', 'OPTIONS'])
def add_Donation():
    """
    Information of a donation transaction which happens betweens two users.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    data : json
        Information about the item which is getting donated.

    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'POST':
        data = json.loads(request.data)
        item_id = data['item_id']
        recipient_id = data['recipient_id']
        status, msg = addDonation(item_id, recipient_id)
        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/donor/history', methods=['POST', 'GET', 'OPTIONS'])
def getDonorInfo():
    """
    Gets information for the current users previous donations.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    id : int
        ID associated with the logged in user.

    Returns
    ----------
    json
        Returns a json containing the status, data which contains the information of the current user's past donations, message in accordance with the status.
    """

    if request.method == 'GET':
        id = request.args.get('id')
        status, data = getDonorHistory(id)
        if status:
            if data == []:
                return jsonify({"status": 200, "data": {}, "message": "No records found"})
            else:
                return jsonify({"status": 200, "data": data, "message": "Donation History Records"})
        else:
            return jsonify({"status": 400, "data": {}, "message": data})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/recipient/history', methods=['POST', 'GET', 'OPTIONS'])
def getRecieverInfo():
    """
    Gets information for all the items received by the user in the past.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    id : int
        ID associated with the currently logged in user.

    Returns
    ----------
    json
        Returns a json containing the status, data which contains the information of the items received by the user in the past, message in accordance with the status.
    """

    if request.method == 'GET':

        id = request.args.get('id')
        status, data = getRecieverHistory(id)
        if status:
            if data == []:
                return jsonify({"status": 200, "data": {}, "message": "No records found"})
            else:
                return jsonify({"status": 200, "data": data, "message": "Donation History Records"})
        else:
            return jsonify({"status": 200, "data": {}, "message": data})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/register', methods=['POST', 'GET', 'OPTIONS'])
def register():
    """
    Register a user.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    data : json
        Information about user who is registering.

    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'POST':
        data = json.loads(request.data)
        name = data['name']
        password = data['password']
        repeatPassword = data['repeatpassword']
        email = data['email']
        city = str(data['city'])
        zipcode = str(data['zipcode'])
        interests = str(data['interests'])

        if (repeatPassword != password):
            return jsonify({"status": 405, "data": {}, "message": "Passwords do not match"})		
        
        check, status = checkDuplicateEmail(email)
        if (status == 0):
            return jsonify({"status": 400, "data": {}, "message": "Error while Accessing the database"})
        if (check):
            return jsonify({"status": 405, "data": {},
                            "message": "Please fill out the form again! The Email is taken/or is written in the wrong format"})

        check = addUser(name, cipher_suite.encrypt(password.encode()), email, city, zipcode, interests)
        if (check):
            return jsonify({"status": 200, "data": {}, "message": "You have registered succesfully"})
        else:
            return jsonify({"status": 400, "data": {}, "message": "Error while adding an user"})
    elif request.method == 'POST':
        return jsonify({"status": 405, "data": {}, "message": "Please fill out the form !"})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/login', methods=['POST', 'GET', 'OPTIONS'])
def login():
    """
    User login.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    data : json
        Information about user who is logging in.

    Returns
    ----------
    json
        Returns a json containing the status, data which contains logged in user's information, message in accordance with the status.
    """

    if request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        password = data['password']
        check, status = loginCheck(email, password)
        if (status == 0):
            return jsonify({"status": 400, "data": {}, "message": "Database Error"})
        if (check):
            userInfo = getUserProfileByEmail(email)
            if (len(userInfo) == 0):
                return jsonify({"status": 400, "data": {}, "message": "Database Error"})
            else:
                return jsonify({"status": 200, "data": userInfo, "message": "Logged in Succesfully"})
        else:
            return jsonify({"status": 405, "data": {}, "message": "Log in error, check credentials"})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/profile', methods=['GET', 'OPTIONS'])
def getProfile():
    """
    Gets the profile of the current user.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    id : int
        ID of the user who is logged in.

    Returns
    ----------
    json
        Returns a json containing the status, data which contains user's information, message in accordance with the status.
    """

    if request.method == 'GET':
        id = request.args.get('id')
        if (id):
            userInfo = getUserProfileByID(id)
            if (len(userInfo) == 0):
                return jsonify({"status": 400, "data": {}, "message": "Database Error"})
            else:
                return jsonify({"status": 200, "data": userInfo, "message": "Profile gotten succesfully"})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/updateprofile', methods=['PUT', 'OPTIONS', 'GET'])
def updateprofile():
    """
    Updates the profile of the current user.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    data : json
        Updated data of the user.

    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """

    if request.method == 'PUT':
        data = json.loads(request.data)

        status, msg = updateProfile(data)

        if status:
            return jsonify({"status": 200, "data": {}, "message": msg})
        else:
            return jsonify({"status": 400, "data": {}, "message": msg})

    return jsonify({"status": 200, "data": {}, "message": ""})

def loginCheck(email, password):
    """
    Checks if the password and email are matching in the database.

    Parameters
    ----------
    email : string
        Email of the user.
    password : string
        Password of the user.

    Returns
    ----------
    tuple
        Returns a tuple with two elements. The first element(a boolean variable) is a check to see if there is a user present with matching password and email. The second element is a status code of whether there is a database error or not.
    """

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
        user = cursor.fetchone()
        boom = cipher_suite.decrypt(user['Password']).decode()
        if user and password==boom:
            return (True, 1)
        else:
            return (False, 1)
    except mysql.connector.Error as error:
        print(error)
        return (False, 0)

    except Exception as e:
        print("some error occurred in loginCheck: {}".format(e))
        return (False, 0)
        # exit("some error occurred in get_items: {}".format(e))

@app.route('/item', methods=['GET', 'OPTIONS'])
def getItem():
    """
    Gets the item details.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side ).\n
    2) Data - Associated data with the operation.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    id : int
        ID of the item.

    Returns
    ----------
    json
        Returns a json containing the status, data which contains user's information, message in accordance with the status.
    """

    if request.method == 'GET':
        id = request.args.get('id')
        if (id):
            itemDetail = getItemByID(id)
            if (len(itemDetail) == 0):
                return jsonify({"status": 400, "data": {}, "message": "Database Error"})
            else:
                return jsonify({"status": 200, "data": itemDetail, "message": "Item gotten succesfully"})

    return jsonify({"status": 200, "data": {}, "message": ""})


@app.route('/getOTP', methods=['POST'])
def getOTP():
    """
    Sending a mail containing the automatically generated OTP.\n
    Response is a json which contains:\n
    1) Status - This can take 3 values = (200 : Perfect response, 405 : Database Error, 400 : Failure from client side, 500:the server encountered an unexpected condition that prevented it from fulfilling the request ).\n
    2) Data - Associated data with the operation, here no data as we expect no response.\n
    3) Message - A message assoicated with the status.

    Parameters
    ----------
    data : json
        Information about the generated OTP along with the mail ID of the yet to be verified user.

    Returns
    ----------
    json
        Returns a json containing the status, data(No data associated with this function, hence the data is empty), message in accordance with the status.
    """
    data = request.get_json()
    otp = data['otp']
    mail = data['mail']
    status, msg = sendmail(mail, otp)
    status = 200 if status else 400
    return jsonify({"status": status, "data": {}, "message": msg})


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)
