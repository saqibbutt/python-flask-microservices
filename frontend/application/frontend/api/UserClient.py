# application/frontend/api/UserClient.py
import requests
from flask import session, request


class UserClient:
    @staticmethod
    def post_login(form):
        api_key = False
        payload = {
            'username': form.username.data,
            'password': form.password.data
        }
        url = 'http://cuser-service:5001/api/user/login'
        response = requests.request("POST", url=url, data=payload)
        if response:
            d = response.json()
            print("This is response from user api: " + str(d))
            if d['api_key'] is not None:
                api_key = d['api_key']
        return api_key

    @staticmethod
    def get_user():

        headers = {
            'Authorization': 'Basic ' + session['user_api_key']
        }
        url = 'http://cuser-service:5001/api/user'
        response = requests.request(method="GET", url=url, headers=headers)
        user = response.json()
        return user

    @staticmethod
    def post_user_create(form):
        user = False
        payload = {
            'email': form.email.data,
            'password': form.password.data,
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'username': form.username.data
        }
        url = 'http://cuser-service:5001/api/user/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            user = response.json()
        return user

    @staticmethod
    def does_exist(username):
        url = 'http://cuser-service:5001/api/user/' + username + '/exists'
        response = requests.request("GET", url=url)
        return response.status_code == 200

