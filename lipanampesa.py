
import requests
from requests.auth import HTTPBasicAuth



import keys
from encode import generate_password
from access_token import generate_access_token
from utils import get_timestamp


formatted_time = get_timestamp()
decoded_password = generate_password(formatted_time)

def lipa_na_mpesa():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": keys.business_shortcode,
    "Password": decoded_password,
    "Timestamp": formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": keys.phone_number,
    "PartyB": keys.business_shortcode,
    "PhoneNumber": keys.phone_number,
    "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
    "AccountReference": "123456",
    "TransactionDesc": "pay for fees "
    }

    response = requests.post(api_url, json = request, headers=headers)

    print (response.text)

lipa_na_mpesa()