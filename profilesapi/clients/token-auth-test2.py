import requests


def client():
    data = {
        'username': 'resttest',
        'email': 'test@mail.com',
        'password1': 'changeme123',
        'password2': 'changeme123'
    }
    response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/',
                             data=data
                             )
    print(f'Status Code: {response.status_code}')
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()
