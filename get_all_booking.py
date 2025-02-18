import requests
from endpoints.base_check_200 import Endpoints

class GetAllBooking(Endpoints):

    def get_all_booking(self):
        self.response = requests.get(f'https://restful-booker.herokuapp.com/booking')
        self.response_json = self.response.json()

