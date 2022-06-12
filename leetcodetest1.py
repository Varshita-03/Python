def sort(posi,seq):
    for i in range(0,posi):
        if seq[i]>seq[posi]:
           ( seq[i],seq[posi])=(seq[posi],seq[i])
    return(seq)
           




num1=[2,5,6]
num2=[1,2,8]
m=len(num1)
n=len(num2)
for k in range(n):
    num1.append(0)
print(num1)
p=1
i=a=j=0
changepos=m-1
while a==0 and j<n:
  i=0
  while i<m+n and a==0:
    if num1[i] > num2[j]:
        pos=num1.count(0)
        print("no. of zeroes:",pos)
        if pos==3:
            changepos=n
        if pos==2:
            changepos=n+1
        if pos==1:
            changepos=n+2
        (num1[i],num1[changepos])=(num1[changepos],num1[i])
        num1[i]= num2[j]
        num1=sort(changepos,num1)
        i=changepos+1
        print("position:",changepos)
        print(num1)
        a=0
    if num1[changepos]<num2[j]:
        for k in range(j,n):
            (num1[changepos+p],num2[k])=(num2[k],num1[changepos+p])
            p=p+1
        a=1
    else:
        i=i+1
        a=0
   
  j=j+1
        

print(num1)
"""Easier way to do the above problem""" 
print("--------Simple Approach--------")      
num1=[2,5,6]
num2=[1,2,8]
m=len(num1)
n=len(num2)
for k in range(n):
    num1.append(0)
print(num1)
for i in range(n):
    pos=num1.count(0)
    print("no. of zeroes:",pos)
    if pos==3:
         changepos=n
    if pos==2:
         changepos=n+1
    if pos==1:
         changepos=n+2
    num1[changepos]=num2[i]
    num1=sort(changepos,num1)
    print(num1)              
                        
                
            
        