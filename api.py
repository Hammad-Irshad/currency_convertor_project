# import requests
# import json



# url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

# curr1 = "INR"
# curr2 = "USD"
# amount = "100"

# querystring = {"from":curr1,"to":curr2,"amount":amount,"symbol":curr2}

# headers = {
# 	"X-RapidAPI-Key": "b2f1c65b6dmsha9ba2116bb0f29ap180815jsnd7d9417231cf",
# 	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
# }

# response = requests.request("GET",url, headers=headers, params=querystring)



# print(response.text)

# data = json.loads(response.text)
# converted_amount = data["result"]["convertedAmount"]

# formatted = "{:,.3f}".format(converted_amount)

# print(converted_amount, formatted)

import requests

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

querystring = {"from":"<REQUIRED>","to":"<REQUIRED>","amount":" "}

headers = {
	"X-RapidAPI-Key": "b2f1c65b6dmsha9ba2116bb0f29ap180815jsnd7d9417231cf",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET",url, headers=headers, params=querystring)

print(response.json())