import requests
from endpoints.base_check_200 import Endpoints

class GetBooking(Endpoints):

    def get_by_id(self, booking_id):
        self.response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
        self.response_json = self.response.json()

    #def check_response_id(self, booking_id):
        #assert  self.response_json['bookingid'] == booking_id

    def check_response_is_404(self):
        assert self.response.status_code == 404