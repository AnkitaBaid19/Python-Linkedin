import requests
print(requests.get(
    'https://api.linkedin.com/v2/jobs',
    params = {
        # Any API params go here
    },
    headers = {
        'Authorization': 'Bearer ' + access_token,
        # Any other needed HTTP headers go here
    },
).json())
