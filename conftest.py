import pytest
from endpoints.create_booking import CreateBooking
from endpoints.delete_booking import DeleteBooking



@pytest.fixture()
def booking_id():
    create_booking = CreateBooking()
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
    create_booking.new_booking(payload)
    yield create_booking.response_json['bookingid']
    delete_booking = DeleteBooking()
    delete_booking.delete_booking(create_booking.response_json['bookingid'])
