#import random to generate random values
#Random is one of the packages
def length(word):
    k=0
    for i in word:
        k=k+1
    return(k)

from random import randint
words=["Ritika","Kori","Karthi","Matcha","Varshitha"]
l=len(words)
k=randint(0,l-1)
print(words[k])
words[k]=list(words[k])
totoption=10
blank=[]
p=length(words[k])
for i in range(p):
    blank.append("_")
print(blank)
while totoption>0 or blank!=words[k]: 
    option=input("Enter your word:")
    for q in range(len(words[k])):
         if option==words[k][q]:
                blank[q]=option
                a=1
                print(blank)
         else:
             a=0
    if a==0:
        totoption=totoption-1
if totoption != 0 and blank!=words[k]:
    print("----Sorry, You lose----")
    
print(blank)
