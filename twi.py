import requests
import datetime
import json

text = ""

POST_CODE = ["400080", "400081", "400082"]
age = 52

# Print details flag
print_flag = 'Y'

numdays = 5
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
print(date_str)

for i in POST_CODE:
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(i, INP_DATE)
        response = requests.get(URL, headers=headers)
        if response.ok:
            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            flag = False
            if resp_json["centers"]:
                print("Available on: {}".format(INP_DATE))
                text += "Available on: {}".format(INP_DATE) + "\n"
                if(print_flag=='y' or print_flag=='Y'):
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if session["min_age_limit"] <= age:
                                print("\t", center["name"])
                                print("\t", center["block_name"])
                                print("\t Price: ", center["fee_type"])
                                print("\t Available Capacity: ", session["available_capacity"])
                                if(session["vaccine"] != ''):
                                    print("\t Vaccine: ", session["vaccine"])
                                print("\n\n")
                                text += "Center Name " + center["name"] + "\n"
                                text += center["block_name"] + "\n"
                                text += "Fee:  " + center["fee_type"] + "\n"
                                text += "Capacity:  " + str(session["available_capacity"]) + "\n"
                                if(session["vaccine"] != ''):
                                    text += "Vaccine Name: " + session["vaccine"] + "\n\n"
                                
            else:
                print("No available slots on {}".format(INP_DATE))
                text += "No available slots on {}".format(INP_DATE) + "\n"
    text += "\n"
print(text)

from twilio.rest import Client 
 
account_sid = 'ACac705688726d9eede317dec0d86f84f9' 
auth_token = '0c73fe3177bab7665d5ec5c745a6ad11' 
client = Client(account_sid, auth_token) 
 
def send_alert():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=f'{text}',      
                                to='whatsapp:+918291523382' 
                            ) 
    
    print(message.sid)


