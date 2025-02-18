import requests
from endpoints.base_check_200 import Endpoints

class PartialUpdateBooking(Endpoints):

    def partial_update_booking(self, booking_id, payload):
        self.response = requests.patch(f'https://restful-booker.herokuapp.com/booking/{booking_id}', json=payload)
        self.response_json = self.response.json()

    def check_response_firstname(self, firstname):
        assert self.response_json['firstname'] == firstname