from googleapiclient import discovery
from google.oauth2 import service_account
import codecs


#This script will connect to the email in which you pass into connect() and create
#a custom signature based on the other arguements you pass in. When Running this
#script, all you need to change is the signature body file paths.



def connect(email, name, job, desig, phone, officephone):
    # Service account credentials and GMAIL API scope for editing signatures

    SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic']
    SERVICE_ACCOUNT_FILE = 'credentials.json'

    # The user we want to "impersonate"

    USER_EMAIL = email

    # Input credentials and delegate credentials to USER_EMAIL

    credentials = service_account.Credentials. \
        from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    delegated_credentials = credentials.with_subject(USER_EMAIL)

    # Connect to the API with the credentals above

    service = discovery.build('gmail', 'v1', credentials=delegated_credentials)

    #count the number of characters of name + designation + title + office phone + personal phone and set the
    #photo length to match

    #ncar = len(name + job + desig + phone + officephone)
    #width = 5.6*ncar

    #Codecs will open the signature_body filepath that we want and pipe in the function arguement 'Name'
    #where we see {Name} in the html file

    base = '/Your Base Folder'

    if desig != '' and phone != '':
        signature_body = base + 'signature_body1.html'
    elif desig != '' and phone == '':
        signature_body = base + 'signature_body2.html'
    elif desig == '' and phone != '':
        signature_body = base + 'signature_body3.html'
    else:
        signature_body = base + 'signature_body4.html'


    # Codecs will open the signature_body filepath that we want and pipe in the function arguements 'name', 'job',
    # 'desig' and 'phone' where we see {name}.. in the html file

    with codecs.open(signature_body, "r") as x:
            signature_body = x.read()
            signature_body = signature_body.format(name=name, job=job, email=email, desig=desig,
                                                   phone=phone, officephone=officephone)


    signature = {'signature' : signature_body}

    # Change the email signature

    rsp = service.users().settings().sendAs().update(userId=email, sendAsEmail=email, body=signature).execute()

    print("Signature changed to '%s'" % rsp['signature'])


