# Needs: python -m pip install requests
import requests, secrets

url = requests.Request(
    'GET',
    'https://www.linkedin.com/oauth/v2/authorization',
    params = {
        'response_type': 'code', # Always should equal to fixed string "code"
        
        # ClientID of your created application
        'client_id': '########' #REPLACE_WITH_YOUR_CLIENT_ID,
        
        # The URI your users are sent back to after authorization.
        # This value must match one of the OAuth 2.0 Authorized Redirect
        # URLs defined in your application configuration.
        # This is basically URL of your server that processes authorized requests like:
        #     https://your.server.com/linkedin_authorized_callback
        'redirect_uri': '#########' #(https://YourServe/auth/linkedin/callback) REPLACE_WITH_REDIRECT_URL
        
        # state, any unique non-secret randomly generated string like DCEeFWf45A53sdfKef424
        # that identifies current authorization request on server side.
        # One way of generating such state is by using standard "secrets" module like below.
        # Store generated state string on your server for further identifying this authorization session.
        'state': secrets.token_hex(8).upper(),
        
        # Requested permissions, below is just example, change them to what you need.
        # List of possible permissions is here:
        #     https://docs.microsoft.com/en-us/linkedin/shared/references/migrations/default-scopes-migration#scope-to-consent-message-mapping
        'scope': '%20'.join(['r_liteprofile', 'r_emailaddress', 'w_member_social']),
    },
).prepare().url

# You may now send this url from server to user
# Or if code runs locally just open browser like below

import webbrowser
webbrowser.open(url)
