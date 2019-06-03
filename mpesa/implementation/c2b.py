import requests
from requests.auth import HTTPBasicAuth
import keys
from my_functions import generate_the_access_token



the_access_token = generate_the_access_token()

def reqister_url():
    # access_token = "Access-Token"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % the_access_token}
    request = {
        "ShortCode": keys.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://iamelvismutende.com/c2b",
        "ValidationURL": "https://iamelvismutende.com/c2b"
        }
    response = requests.post(api_url, json = request, headers=headers)

    return response.text


# print(reqister_url())

def simulate_c2b_transaction():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % the_access_token}
    request = { 
    "ShortCode":keys.shortcode,
    "CommandID":"CustomerPayBillOnline",
    "Amount":"2",
    "Msisdn":keys.test_msisdn,
    "BillRefNumber":"32415138" 
    }

    response = requests.post(api_url, json = request, headers=headers)

    return (response.text)

print(simulate_c2b_transaction())