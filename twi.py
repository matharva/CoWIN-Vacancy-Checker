from twilio.rest import Client 
 
account_sid = 'ACac705688726d9eede317dec0d86f84f9' 
auth_token = '0c73fe3177bab7665d5ec5c745a6ad11' 
client = Client(account_sid, auth_token) 
 
def send_alert():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Hemlo',      
                                to='whatsapp:+918291523382' 
                            ) 
    
    print(message.sid)