import requests

url = "https://api.apilayer.com/currency_data/change?start_date={start_date}&end_date={end_date}"


response = requests.get(url)
print(response)
data=response.json()
result = response.text
print(result)
print(data.keys())
print(data.values())