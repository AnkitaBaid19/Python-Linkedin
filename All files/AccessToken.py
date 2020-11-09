# Needs: python -m pip install requests
import requests
access_token = requests.post(
    'https://www.linkedin.com/oauth/v2/accessToken',
    params = {
        'grant_type': 'authorization_code',
        # This is code obtained on previous step by Python script.
        'code': '######################################' #REPLACE_WITH_CODE,
        # This should be same as 'redirect_uri' field value of previous Python script.
        'redirect_uri': '#####' #(https://YourServe/auth/linkedin/callback) REPLACE_WITH_REDIRECT_URL,
        # Client ID of your created application
        'client_id': '#########' #REPLACE_WITH_YOUR_CLIENT_ID',
        # Client Secret of your created application
        'client_secret': '###########' #REPLACE_WITH_YOUR_CLIENT_SECRET,
    },
).json()
print(access_token)
