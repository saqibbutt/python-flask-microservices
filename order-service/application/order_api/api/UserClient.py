# application/order_api/api/UserClient.py
import requests


class UserClient:
    @staticmethod
    def get_user(api_key):
        headers = {
            'Authorization': api_key
        }
        response = requests.request(method="GET", url='http://cuser-service:5001/api/user', headers=headers)
        if response.status_code == 401:
            return False
        user = response.json()
        return user
