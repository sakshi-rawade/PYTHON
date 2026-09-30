''' if-else'''
marks =int(input("Enter the marks:"))
if marks >=40:
    print("Pass")
else:
    print("Better luck next time")
    
print("-----------------------------------------------------------------")
'''if-elif-else'''
marks=int(input("Enter Marks:"))
    
if marks>=75 :
        print("Distinction")
elif marks >=60:
        print("First Class")
elif marks >=40:
        print("Pass")
else:
        print("Next Time Bhaiii")
        
print("-------------------------------------------------------------------")    

''' for loop'''
''' include point of include and exclude here '''
for i in range(5):
    print(" welcomee welcomee")
print("---------------------------------------------------")
for i in range(1,6):
     print(i)
print("-----------------------------------------------------------")

'''multiplication table'''
num=int(input("Enter the number:"))
for i in range(1,11):
    print(num ,"x", i,"=",num*i )
print("----------------------------------------------")

''' while loop'''  
''' repeats until loop is true '''
count =1

while count <=5:
    print(count)
    count+=1
print("----------------------------------")
'''nested control statment '''
for i in range(1,6):
    if i % 2==0:
        print(i,"is Even")
    else:
        print(i,"is Odd")
print("--------------------------------------------------")

'''Mini Practice'''   
# print numbers from 1 to 10
for i in range (1,11):
    print(i)
 #print even number 
for i in range(2,21,2):
     print(i)
#countdown 
count=10
while count >0:
    print(count)
    count-=1
print("Launch!!")     