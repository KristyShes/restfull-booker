import requests
from endpoints.base_check_200 import Endpoints

class HealthCheck(Endpoints):

    def health_check(self):
        self.response = requests.get(f'https://restful-booker.herokuapp.com/ping')
        self.response_json = self.response.json()
