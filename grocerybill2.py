"""Grocery bill"""
def grocerybill():
   print("Please enter your list of items:")
   item1=input("Enter your first item:")
   lists=[item1]
   m=input("Do you want to continue[Y/N]:")
   while(m=='Y'):
      item=input("Enter your next item:")
      lists.append(item)
      m=input("Do you want to continue[Y/N]:")
   lists.sort()
   print("-------Your grocery bill-----")
   for i in range(len(lists)):
      if not (lists[i]=='Flour'):
           print(lists[i],":",lists.count("Flour")*10)
      if not (lists[i]=='Rice'):
           print(lists[i],":",lists.count("Rice")*5)
      if not (lists[i]=='Butter'):
           print(lists[i],":",lists.count("Butter")*30)
      if not (lists[i]=='Bread'):
           print(lists[i],":",lists.count("Bread")*10)
      if not (lists[i]=='Chocolate'):
          print(lists[i],":",lists.count("Chocolate")*15)
   p=lists.count("Flour")*10+lists.count("Rice")*5+lists.count("Butter")*30+lists.count("Bread")*10+lists.count("Chocolate")*15
   print("-->Total Bill:",p)
   print("------Thanks for shopping",n,"--------")

print("Welcome to online grocery!!")
n=input("Your name:")
print("Hii,",n)
grocerybill()   