# Change-Company-Email-Sig
Change your company wide email signature with custom information for each employee

Roadmap 

admin_directory.py -- Initiates an admin sdk request. In this example, I am using a service account that has company wide priveledges. Anytime a service account wants to do anything, it needs to initiate an an admin sdk request, which will either get accepted or denied based on the priveldges you assign to it. 

credentials.py -- Where all you credentials are defined.

sheets.py - Uses the google sheets API to allow you to pull data form a specified google sheet. This is sheet is where you should keep a running list of employees and their information.

email_sig.py -- Takes the information (name, title, email, etc) defined in your google sheet, logs into a users account with the specified service account, finds gmail signature setting, and changes the signature to refelct the information/variables in the google sheet.
