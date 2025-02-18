import requests
import pytest
from endpoints.partial_update_booking import PartialUpdateBooking
from endpoints.get_booking import GetBooking
from endpoints.update_booking import UpdateBooking
from endpoints.get_all_booking import GetAllBooking
from endpoints.create_booking import CreateBooking
from endpoints.base_create_token import CreateToken
from endpoints.delete_booking import DeleteBooking
from endpoints.get_booking_ids import GetBookingIds
from endpoints.health_check import HealthCheck

def test_create_token():
    new_token_endpoint = CreateToken()
    payload = {
        "username": "admin",
        "password": "password123"
    }
    new_token_endpoint.new_token(payload=payload)
    new_token_endpoint.check_response_is_200()
    new_token_endpoint.check_username(payload['username'])


def test_create_booking():
    new_booking_endpoint = CreateBooking()
    payload = {
        "firstname" : "Jimmy",
        "lastname" : "Browner",
        "totalprice" : 124,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2025-01-01",
            "checkout" : "2025-02-01"
        },
        "additionalneeds" : "Breakfast"
    }
    new_booking_endpoint.new_booking(payload=payload)
    new_booking_endpoint.check_response_is_200()
    new_booking_endpoint.check_firstname(payload['firstname'])


def test_get_booking(booking_id):
    get_booking_endpoint = GetBooking()
    get_booking_endpoint.get_by_id(booking_id)
    get_booking_endpoint.check_response_is_200()
    #get_booking_endpoint.check_response_id(booking_id)

def test_get_all_booking():
    get_all_booking_endpoint = GetAllBooking()
    get_all_booking_endpoint.check_response_is_200()

def test_get_booking_ids():
    get_booking_ids_endpoint = GetBookingIds()
    qwery = {"firstname": "Jammy", "lastname": "Brown"}
    get_booking_ids_endpoint.get_by_firstname_last_name(params=qwery)
    get_booking_ids_endpoint.check_response_is_200()
    get_booking_ids_endpoint.check_response_firstname(qwery['firstname'])
    get_booking_ids_endpoint.check_response_lastname(qwery['lastname'])


def test_update_booking(booking_id):
    update_booking_endpoint = UpdateBooking()
    payload = {
        "firstname" : "Jammy",
        "lastname" : "Browner",
        "totalprice" : 150,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2025-01-01",
            "checkout" : "2025-02-01"
        },
        "additionalneeds" : "Breakfast"
    }
    update_booking_endpoint.update_booking(booking_id, payload)
    update_booking_endpoint.check_response_is_200()
    update_booking_endpoint.check_response_firstname(payload['firstname'])

def test_partial_update_booking(booking_id):
    partial_update_booking_endpoint = PartialUpdateBooking()
    payload = {
        "firstname" : "James",
        "lastname" : "Brown"
    }
    partial_update_booking_endpoint.partial_update_booking(booking_id, payload)
    partial_update_booking_endpoint.check_response_is_200()
    partial_update_booking_endpoint.check_response_firstname(payload['firstname'])

def test_delete_booking(booking_id):
    delete_booking_endpoint = DeleteBooking()
    delete_booking_endpoint.delete_booking(booking_id)
    delete_booking_endpoint.check_response_is_200()
    get_booking_endpoint = GetBooking()
    get_booking_endpoint.get_by_id(booking_id)
    get_booking_endpoint.check_response_is_404()

def test_health_check():
    health_check_endpoint = HealthCheck()
    health_check_endpoint.check_response_is_200()


