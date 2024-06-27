import requests

# Define the base URL
base_url = 'https://jsonplaceholder.typicode.com/posts'

# GET request
try:
    response = requests.get(f'{base_url}/1')
    response.raise_for_status()
    print('GET:', response.json())
except requests.exceptions.RequestException as e:
    print(f'GET request failed: {e}')

# POST request
try:
    payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.post(base_url, json=payload)
    response.raise_for_status()
    print('POST:', response.json())
except requests.exceptions.RequestException as e:
    print(f'POST request failed: {e}')

# PUT request
try:
    payload = {'id': 1, 'title': 'foo', 'body': 'bar', 'userId': 1}
    response = requests.put(f'{base_url}/1', json=payload)
    response.raise_for_status()
    print('PUT:', response.json())
except requests.exceptions.RequestException as e:
    print(f'PUT request failed: {e}')

# DELETE request
try:
    response = requests.delete(f'{base_url}/1')
    response.raise_for_status()
    print('DELETE:', response.status_code)
except requests.exceptions.RequestException as e:
    print(f'DELETE request failed: {e}')
