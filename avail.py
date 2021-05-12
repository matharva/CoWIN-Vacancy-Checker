import requests
import datetime
import json

POST_CODE = ["400080", "400081", "400082"]
age = 52

# Print details flag
print_flag = 'Y'

numdays = 5
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
print( date_str)

for i in POST_CODE:
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(i, INP_DATE)
        print("Hello")
        response = requests.get(URL, headers=headers)
        print(response)
        if response.ok:
            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            flag = False
            if resp_json["centers"]:
                print("Available on: {}".format(INP_DATE))
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
                                
                
                    
            else:
                print("No available slots on {}".format(INP_DATE))