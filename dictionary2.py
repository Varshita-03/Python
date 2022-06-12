#dictionary
#nested dicionary
""" 1: Studies
    2: Sports
    3: Discipline
    4: Projects  """
perform={1:{1:34,2:72,3:90,4:100},
         2:{1:100,2:92,3:92,4:70},
         3:{1:34,2:100,3:44,4:100},
         4:{1:50,2:90,3:34,4:100},
         5:{}                    }
l=[]
rollno=input("Enter Student roll no.:")
rollno=int(rollno)
detail=input("Enter the specific domain no. to view its performance:")
detail=int(detail)
print(perform[rollno][detail])
print(perform.keys())
print(type(perform))
print(perform.values())
choice=input("Do you want to change any data?[Y/N]:")
if choice=='Y':
    roll=input("Enter Roll no. of the student:")
    roll=int(roll)
    detail=input("Enter the domain:")
    detail=int(detail)
    changevalue=input("Enter the updated value:")
    changevalue=int(changevalue)
    perform[roll][detail]=changevalue
else:
    print("-----Thank you-----")
print(perform.values())
for i in range(1,5):
    newvalue=input("Enter new student marks:")
    newvalue=int(newvalue)
    l.append(newvalue)
    perform[5][i]=l[i-1]
print(perform.keys())
print(perform.values())
