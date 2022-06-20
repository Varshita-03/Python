import requests
import bs4
import lxml.etree as xml

url="https://github.com/requests/requests"
response= requests.get(url)
#print(response)
#print(response.text)

web_page= bs4.BeautifulSoup(response.text, "lxml")#converting into lxml
print(type(web_page))
print(web_page.head.title.text)#The content in the head command
#Converts it into text form
print(web_page.body.template)

sub_page=web_page.find_all(name="ul")
print(sub_page[3])





