#external packaages 

#pip install requests 

import requests

response =requests.get("https://example.com/customers/101" )
if response.status_code ==200:
    customer =response.jsom()
    print(customer)