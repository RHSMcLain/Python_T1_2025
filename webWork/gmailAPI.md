# Using Gmail API
 [Reference](https://developers.google.com/workspace/gmail/api/quickstart/python)
 ## Step 1: Follow reference instuctions to enable the API
- Save the secrets file into your project folder as 'credentials.json'


 ## Step 2: Include OAuth Requirements
 ### Includes for Oauth
    import os.path 
*Helps find the right files for Oauth
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
- Remember to set the SCOPES to https://www.googleapis.com/auth/gmail.send
 ## Step 3: Include email send code

