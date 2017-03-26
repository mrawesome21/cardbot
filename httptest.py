import http.client
import json
def createcustomer(client, firstname, lastname, streetnum, streetname, city, state, zipcode):
    s = {"first_name": "John","last_name": "Doe","address": {"street_number": "1111","street_name": "Baker Street","city": "Vienna","state": "VA","zip": "22182"}}

    js = json.dumps(s)
    
    headers = {"Content-type": "application/json", "Accept": "application/json"}
    client.request("POST", "/customers?key=871a79ef8082ee4538025e07513c9c5f",body=js,headers=headers)    

def createaccount(client, _id, _type, nickname, rewards, balance, accountnumber, customerid):
    info = {"id": "871a79ef8082ee4538025e07513c9c5f","type": "Credit Card","nick_name": "Venture Rewards","_rewards": "40000","_balance": "0"}
    
    js = json.dumps(s)
    
    headers = {"Content-type": "application/json", "Accept": "application/json"}
    
    client.request("POST", "/customers?key=871a79ef8082ee4538025e07513c9c5f",body=js,headers=headers) 
    
h1 = http.client.HTTPConnection('api.reimaginebanking.com')
createcustomer(h1, "John", "Doe", "1111", "WOW AVENUE", "Vienna", "VA", "22182")
r = h1.getresponse()
print(r.status, r.reason)


