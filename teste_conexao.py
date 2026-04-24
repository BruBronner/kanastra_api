import requests

url = "https://data-service-sandbox.kanastra.com.br/v2/auth"

headers = {
    "Content-Type": "application/json",
    "merchant_id": "SEU_MERCHANT_ID"
}

body ={
  "client_id": "string", # o client id
  "client_secret": "string" # o secret id
}

response = requests.post(url, headers=headers, json=body)

print(response.status_code)
print(response.json())