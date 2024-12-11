import requests
class APIS:
    base_url = 'https://reqres.in/api/users?page=2'

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
        }

    def get(self, endpoint=''):
        # Construct the full URL
        url = f'{self.base_url}/{endpoint}' if endpoint else self.base_url
        response = requests.get(url, headers=self.headers)
        return response


