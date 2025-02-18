import pytest
import requests
import json

@pytest.fixture()
def booking_id():
    payload = {
        "firstname": "Jimmy",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f'https://restful-booker.herokuapp.com/booking', json=payload).json()
    yield response['bookingid']
    requests.delete(f'https://restful-booker.herokuapp.com/booking/{response["bookingid"]}')

@pytest.fixture()
def token():
    payload = {
        "username" : "admin",
        "password" : "password123"
    }
    response = requests.post(f'https://restful-booker.herokuapp.com/auth', json=payload).json()
    return response['token']

def test_create_booking(token):
    payload = {
        "firstname" : "Jimmy",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(f'https://restful-booker.herokuapp.com/booking', json=payload).json()
    return response['bookingid']

def test_get_booking(token, booking_id):
    print(booking_id)
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
    assert response.status_code == 200

def test_get_all_booking():
    response = requests.get(f'https://restful-booker.herokuapp.com/booking')
    assert response.status_code == 200

def test_get_booking_name():
    qwery = {"firstname": "sally", "lastname": "browm"}
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/', params=qwery).json()

def test_get_booking_date():
    qwery = {"checkin": 2014 - 0o3 - 13, "checkout": 2014 - 0o5 - 21}
    response = requests.get(f'https://restful-booker.herokuapp.com/booking', params=qwery).json()

def test_update_booking(token, booking_id):
    payload = {
        "firstname" : "James",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.put(f'https://restful-booker.herokuapp.com/booking/{booking_id}', json=payload).json()
    assert response['firstname'] == payload['firstname']

def test_partial_update_booking(token, booking_id):
    payload = {"firstname" : "Jamys", "lastname" : "Brown"}
    response = requests.patch(f'https://restful-booker.herokuapp.com/booking/{booking_id}', json=payload).json()
    assert response['lastname'] != payload['lastname']

def test_delete_booking(token, booking_id):
    response = requests.delete(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
    assert response.status_code == 201
    response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
    assert response.status_code == 404









