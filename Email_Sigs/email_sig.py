import pandas as pd
from credentials import connect
import numpy as np


#Define the csv (list of employees) to pass into the connect() method
#would also need to change the pathname here

EmailList = pd.read_csv('Path to a CSV containing an employee list',
                        usecols=['Name', 'Designation', 'Title', 'Email', 'Office Number', 'Personal Number'])

EmailList = EmailList.replace(np.nan, '', regex=True)

#iterate over all rows in the Email List

for row in range(0, EmailList.shape[0]):
     connect(name=EmailList['Name'][row], desig=EmailList['Designation'][row], email=EmailList['Email'][row], job=EmailList['Title'][row],
             officephone=EmailList['Office Number'][row], phone=EmailList['Personal Number'][row])


#print(EmailList)