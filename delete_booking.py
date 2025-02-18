import requests
from endpoints.base_check_200 import Endpoints

class DeleteBooking(Endpoints):

    def delete_booking(self, booking_id):
        self.response = requests.delete(f'https://restful-booker.herokuapp.com/booking/{booking_id}')
        self.response_json = self.response.json()

    def check_response_is_404(self):
        assert self.response.status_code == 404