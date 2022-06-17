# Code is generated using Postman app
# Joke API
import requests

url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,racist,sexist,explicit"
response = requests.get(url)
print(response)

# Response 200 communication established
# Response 404 Error in URL
# Convert into human redable form
received_Data=response.json()
print(received_Data)

#the data format is dictionary
print("Category printing:",received_Data.values())
#dictionary properties can be applied

for data in received_Data.keys():
    if data=="id" or data=="type" or data=="flags" or data=="error" or data=="category":
        continue
    print("{}:{}".format(data,received_Data[data]))
