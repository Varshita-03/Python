"""Program on loops"""
"""Grocery shopping website"""
print("Welcome to the online kiran")
print("The cheapest shopping website with 0 delivery charges")
s=input("First name:")
p=input("Last name:")
print("Please provide your grocery list here",s)
shopping=input("First item:")
lists=[shopping]
a="N"
while(a=="N"):
    s1=input("Second item:")
    lists.append(s1)
    s2=input("Third item:")
    lists.append(s2)
    s3=input("Fourth item:")
    lists.append(s3)
    s4=input("Fifth item:")
    lists.append(s4)
    a=input("Do you want to make the bill(Y/N):")
lists.sort()
lists.reverse()
print("------The bill-----")
print("Customer Name:",s,p)
for i in range(len(lists)):
    if(lists[i]=="Bread"):
        print(lists[i],"price=",lists.count("Bread")*5,"$")
    if(lists[i]=="Butter"):
        print(lists[i],"price=",lists.count("Butter")*10,"$")
    if(lists[i]=="Ghee"):
        print(lists[i],"price=",lists.count("Ghee")*15,"$")
    if(lists[i]=="Biscuits"):
        print(lists[i],"price=",lists.count("Biscuits")*3,"$")
    if(lists[i]=="Flour"):
        print(lists[i],"price=",lists.count("Flour")*50,"$")
    if(lists[i]=="Rice"):
        print(lists[i],"price=",lists.count("Rice")*100,"$")
    if(lists[i]=="Chocolate"):
        print(lists[i],"price=",lists.count("Chocolate")*12,"$")
    if(lists[i]=="Apple"):
        print(lists[i],"price=",lists.count("Apple")*100,"$")
print("Total items=",len(lists))
"""Len is used to determine the length of the lists"""
"""Sort is used to sort the list in a certain order"""
"""Reverse is used to reverse the order of the list"""

