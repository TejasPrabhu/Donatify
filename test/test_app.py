import unittest
from unittest.mock import patch
import json
from urllib import response

from src.Backend.app import app


class TestApp(unittest.TestCase):
    def test_register_get(self):
        tester = app.test_client(self)
        response = tester.get("/register")
        expected = {'data': {}, 'message': '', 'status': 200}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_updateprofile_get(self):
        tester = app.test_client(self)
        response = tester.get("/updateprofile")
        expected = {'data': {}, 'message': '', 'status': 200}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_login_get(self):
        tester = app.test_client(self)
        response = tester.get("/login")
        expected = {'data': {}, 'message': '', 'status': 200}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_addDonation_get(self):
        tester = app.test_client(self)
        response = tester.get("/addDonation")
        expected = {'data': {}, 'message': '', 'status': 200}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_updateitem_get(self):
        tester = app.test_client(self)
        response = tester.get("/updateitem")
        expected = {'data': {}, 'message': '', 'status': 200}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_additem_get(self):
        tester = app.test_client(self)
        response = tester.get("/additem")
        expected = {'data': {}, 'message': '', 'status': 200}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_emptyroute_get(self):
        tester = app.test_client(self)
        response = tester.get("/")
        expected = {"status": 200, "data": {}, "message": "Backend working"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_updateprofile_put(self):
        tester = app.test_client(self)
        inpData = {"name": "Sam", "email": "sam@gmail.com", "city": [
            "Raleigh", "Durham"], "zipCodes": ["27606"], "interests": ["Food"], "id": 2}
        response = tester.put("/updateprofile", data=json.dumps(inpData),
                              headers={'content-type': 'application/json'})
        expected = {"status": 200, "data": {},
                    "message": "Record updated successfully into item table"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_getProfile_get(self):
        tester = app.test_client(self)
        response = tester.get('/profile?id=1')
        expected = {"status": 200,
                    "data": {'city': 'Raleigh', 'email': 'abc@gmail.com',
                             'interests': '["food", "furniture", "appliance", "electronics"]',
                             'name': 'ABC', 'password': '1234567', 'zipcode': '27606'},
                    "message": "Profile gotten succesfully"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_login_post_1(self):
        tester = app.test_client(self)
        inpData = {"email": "sam@gmail.com", "password": "sam"}
        response = tester.post("/login", data=json.dumps(inpData),
                               headers={'content-type': 'application/json'})
        expected = {"status": 405, "data": {},
                    "message": "Incorrect email/Password"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_login_post_2(self):
        tester = app.test_client(self)
        inpData = {"email": "abc@gmail.com", "password": "1234567"}
        response = tester.post("/login", data=json.dumps(inpData),
                               headers={'content-type': 'application/json'})
        expected = {"status": 200,
                    "data": {"name": "ABC", "email": "abc@gmail.com", "city": "Raleigh", "zipcode": "27606",
                             "interests": '["food", "furniture", "appliance", "electronics"]', "ID": 1},
                    "message": "Logged in Succesfully"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_register_post_1(self):
        tester = app.test_client(self)
        inpData = {"name": "Sam", "email": "sam@gmail.com", "city": [
            "Raleigh", "Durham"], "zipcode": ["27606"], "interests": ["Food"], "ID": 3, "password": "sam", "repeatpassword": "saam"}
        response = tester.post("/register", data=json.dumps(inpData),
                               headers={'content-type': 'application/json'})
        expected = {"status": 405, "data": {},
                    "message": "Passwords do not match"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_register_post_2(self):
        tester = app.test_client(self)
        inpData = {"name": "Sam", "email": "abc@gmail.com", "city": [
            "Raleigh", "Durham"], "zipcode": ["27606"], "interests": ["Food"], "ID": 3, "password": "sam", "repeatpassword": "sam"}
        response = tester.post("/register", data=json.dumps(inpData),
                               headers={'content-type': 'application/json'})
        expected = {"status": 405, "data": {
        }, "message": "Please fill out the form again! The Email is taken/or is written in the wrong format"}
        assert expected == json.loads(response.get_data(as_text=True))

    @patch('src.Backend.app.addUser')
    @patch('src.Backend.app.checkDuplicateEmail')
    def test_register_post_3(self, mock_checkDuplicateEmail, mock_addUser):
        tester = app.test_client(self)
        mock_checkDuplicateEmail.return_value = False, 1
        mock_addUser.return_value = True
        inpData = {"name": "Sam", "email": "sam@gmail.com", "city": [
            "Raleigh", "Durham"], "zipcode": ["27606"], "interests": ["Food"], "ID": 3, "password": "sam", "repeatpassword": "sam"}
        response = tester.post("/register", data=json.dumps(inpData),
                               headers={'content-type': 'application/json'})
        expected = {"status": 200, "data": {},
                    "message": "You have registered succesfully"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_getReceiverInfo_1(self):
        tester = app.test_client(self)
        response = tester.get("/recipient/history?id=1000000")
        expected = {"status": 200, "data": {}, "message": "No records found"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_getReceiverInfo_2(self):
        tester = app.test_client(self)
        response = tester.get("/recipient/history?id=2")
        expected = {"status": 200,
                    "data": {'itemId': 1, 'itemName': 'book', 'itemQuantity': 2, 'itemDescription': 'old books',
                             'itemZipCode': '27606', 'itemCity': 'Raleigh', 'itemDonorId': 1, 'itemDonorName': 'ABC',
                             'itemCategory': 'furniture'},
                    "message": "Donation History Records"}
        assert expected['status'] == response.json['status']
        assert expected['data'] in response.json['data']
        assert expected['message'] == response.json['message']

    def test_getDonorInfo_1(self):
        tester = app.test_client(self)
        response = tester.get("/donor/history?id=1000000")
        expected = {"status": 200, "data": {}, "message": "No records found"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_getDonorInfo_2(self):
        tester = app.test_client(self)
        response = tester.get("/donor/history?id=1")
        expected = {"status": 200,
                    "data": {'itemCategory': 'furniture', 'itemCity': 'Raleigh',
                              'itemDescription': 'old books', 'itemDonorId': 1, 'itemId': 1, 'itemName': 'book',
                              'itemQuantity': 2, 'itemZipCode': '27606'},
                    "message": "Donation History Records"}
        assert expected['status'] == response.json['status']
        assert expected['data'] in response.json['data']
        assert expected['message'] == response.json['message']

    def test_add_Donation(self):
        tester = app.test_client(self)
        inpData = {"item_id": 1000, "recipient_id": 1000}
        response = tester.post("/addDonation", data=json.dumps(inpData),
                               headers={'content-type': 'application/json'})
        expected = {"status": 200, "data": {},
                    "message": "Record inserted successfully into donation table"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_updateitem(self):
        tester = app.test_client(self)
        inpData = {"item_name": "Rice", "quantity": 1, "description": "Rice",
                   "zipcode": "27605", "city": "Raleigh", "donor_id": 3, "category": "Food", "item_id": 2}
        response = tester.put("/updateitem", data=json.dumps(inpData),
                              headers={'content-type': 'application/json'})
        expected = {"status": 200, "data": {},
                    "message": "Record updated successfully into item table"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_additem(self):
        tester = app.test_client(self)
        inpData = {"item_name": "Rice", "quantity": 1, "description": "Rice",
                   "zipcode": "27605", "city": "Raleigh", "donor_id": 3, "category": "Food"}
        response = tester.post("/additem", data=json.dumps(inpData),
                               headers={'content-type': 'application/json'})

        expected = {"status": 200, "data": {},
                    "message": "Record inserted successfully into item table"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/items?id=1&page=100")
        expected = {"status": 200, "data": {}, "message": "No more data"}
        assert expected == json.loads(response.get_data(as_text=True))

    def test_home_1(self):
        tester = app.test_client(self)
        response = tester.get("/items?id=1&page=1")
        expected = {"status": 200,
                    "data": {'donorEmail': 'abc@gmail.com', 'itemCategory': 'furniture', 'itemCity': 'Raleigh',
                             'itemDescription': 'old books', 'itemDonorId': 1, 'itemId': 1, 'itemName': 'book',
                             'itemQuantity': 2, 'itemZipCode': '27606'},
                    "message": "Fetched records successfully"}
        assert expected['status'] == response.json['status']
        assert expected['data'] in response.json['data']
        assert expected['message'] == response.json['message']
