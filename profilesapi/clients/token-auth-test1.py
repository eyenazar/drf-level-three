import requests


def client():
    token_h = 'Token 1526372e7ff4483d58723547331b4eb0c2422dd2'
    # credentials = {'username': 'admin', 'password': '12345'}
    #
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)

    headers = {'Authorization': token_h}
    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print(f'Status Code: {response.status_code}')
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
