''' variables declaration'''

customer_name = "Sakshi"
age =22
premium = 25000.50
active =True 

print("Customer:",customer_name)
print("Age :", age)
print("Premium:",premium)
print("Active:",active)

print("----------------------------------------------------------------------------")

''' types of the variables declared'''
print(type(customer_name))
print(type(age))
print(type(premium))
print(type(active))

print("----------------------------------------------------------------------------")

''' premium calculation '''
sum_assured =10000
rate=0.05
premium =sum_assured *rate
print("Premium:",premium)


print("----------------------------------------------------------------------------")
''' update premium'''
premium =25000
premium += 2000
print("Updates Premium :",premium)


print("----------------------------------------------------------------------------")

''' Taking input from users'''
name=input("Enter Customer Name:")
age=int(input("Enter age:"))
premium=float(input("Enter Premium:"))

print(name)
print(age)
print(premium)
