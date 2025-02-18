import requests

class CreateToken:


    def new_token(self, payload):
        self.response = requests.post(f'https://restful-booker.herokuapp.com/auth', json=payload)
        self.response_json = self.response.json()

    def check_username(self, username):
        assert self.response_json['username'] == username

