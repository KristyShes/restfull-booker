import requests
import query
from endpoints.base_check_200 import Endpoints

class GetBookingIds(Endpoints):

    def get_by_firstname_last_name(self, lastname, firstname):
        self.response = requests.get(f'https://restful-booker.herokuapp.com/booking/', params=query)
        self.response_json = self.response.json()

    def check_response_lastname(self, lastname):
        assert self.response_json['lastname'] == lastname

    def check_response_firstname(self, firstname):
        assert self.response_json['firstname'] == firstname

    def check_response_is_404(self):
        assert self.response.status_code == 404


