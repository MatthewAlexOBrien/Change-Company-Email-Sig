from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


#Everytime you want to access an admin sdk object, you need to intitiate an admin sdk request
#with your credentials, which is exactly what this script will do.


# Email of the Service Account
SERVICE_ACCOUNT_EMAIL = 'email-signature@email-signatures-259817.iam.gserviceaccount.com'

# Path to the Service Account's Private Key file
SERVICE_ACCOUNT_PKCS12_FILE_PATH = '/Users/matthewobrien/Dropbox (BEworks)/HR - Organization/Python Projects/Email_Sigs/Email_Script_Key.p12'

def create_directory_service(user_email):
    """Build and returns an Admin SDK Directory service object authorized with the service accounts
    that act on behalf of the given user.

    Args:
      user_email: The email of the user. Needs permissions to access the Admin APIs.
    Returns:
      Admin SDK directory service object.
    """

    credentials = ServiceAccountCredentials.from_p12_keyfile(
        SERVICE_ACCOUNT_EMAIL,
        SERVICE_ACCOUNT_PKCS12_FILE_PATH,
        'notasecret',
        scopes=['https://www.googleapis.com/auth/admin.directory.user'])

    credentials = credentials.create_delegated(user_email)

    return build('admin', 'directory_v1', credentials=credentials)

create_directory_service('matthew.obrien@beworks.com')