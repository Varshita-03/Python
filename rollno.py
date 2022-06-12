""" ERP PORTAL
    Roll no. assingnment
    Purpose of visit to campus
"""

print("Welcome to erp IIT KGP")
n=input("Enter your name:")
m=input("Year of joining(only the last two digits):")
p=input("Enter branch code:")
q=input("Enter B.tech or M.tech:")
if(q=='B.tech'):
     r='1'
if(q=='M.tech'):
     r='3'
s=input("Enter your room no:")
a=int(s)
if(a<100):
    print(n,"Your roll no is:",m+p+r,"00",s)
if(a>=100):
    print(n,"Your roll no is:",m+p+r,"0",s)
print("Welcome",n,"!")
m=input("Purpose of visit to campus:") 
if(m=='Resource constraint student'):
    print("Thank you",n,"!will be directing to the portal") 
else:
    print("Sorry.Access denied.")