import requests
from endpoints.base_check_200 import Endpoints

class CreateBooking(Endpoints):

    def new_booking(self, payload):
        self.response = requests.post(f'https://restful-booker.herokuapp.com/booking', json=payload)
        self.response_json = self.response.json()

    def check_firstname(self, firstname):
        assert self.response_json['firstname'] == firstname