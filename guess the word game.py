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
totoption=5
blank=[]
p=length(words[k])
a=0
for i in range(p):
    blank.append("_")
print(blank)
while totoption>0 and blank!=words[k]:
    a=0
    option=input("Enter your word:")
    for q in range(len(words[k])):
         if option==words[k][q]:
                blank[q]=option
                print(blank)
         else:
             a=a+1
    if a==len(words[k]):
        totoption=totoption-1
        print("----Wrong Answer----")
    print("Attempts remaining:",totoption)
    
if totoption== 0:
    print("----Sorry, You lose----")
if blank==words[k]:
    print("*****YOU WIN!******")
    
print(blank)
