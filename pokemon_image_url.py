#Pokemon API
import requests
poke_name=input("Enter your pokemon name:")
url = ("https://api.pokemontcg.io/v1/cards?name={}". format(poke_name))


response = requests.get(url)
print(response)
data=response.json()
print(data["cards"][0]["imageUrl"])

import matplotlib.pyplot as plt
url1=data["cards"][2]["imageUrl"]
data1=requests.get(url1)
with open("./pokemon.png","wb") as f:
    for item in data1.iter_content(1024):#iter for iteration of content in link
             f.write(item)
image_data=plt.imread("./pokemon.png")
plt.imshow(image_data)

#Everytime we change the image the file gets overwritten
#to get a photo of the pokemon we have to use matplotlib
