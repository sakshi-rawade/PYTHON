#Functions
# def keyword is used to create function

#create function 
def welcome(name):
    print("Welcome ",name)


#funtion call
def greet():
    print("Welcome to Transflower..")
greet()

#function with parameters 
def Student(name,course):
    print(name,"is learning",course)
Student("Skshi",'Ds')
Student("Soham","cricket")

#returning values 
def add(a,b):
    return a+b
result= add(20,30)
print(result)

#square of a number 
def square(number):
    return number *number
print(square (8))

#variable scope 
def demo():
    message ="Hello"
    print(message)
demo()

#globl variables
college ='Transflower'

def display():
    print(college)
    
display()

#functional arguments 
#positional arguments
def multiply(a,b):
    print(a*b)
multiply(5,4)

#keyword arguments
def employee(name,department):
    print(name,department)
employee(department ="HR",name="Sakshi")

#Default arguments 
def greet(name="Student"):
    print("Welcome",name)
greet()
greet("Sak")


#Mini Prcatice 
#Function to Find Maximum 
def maximum(a, b):
    if a>b:
        return a 
    return b 
print(maximum(15,10))

#function to check even number 
def isEven(number):
    return number % 2==0
print(isEven(20))

#Calculate Area
def area(length,width):
    return length * width
print(area (12,5))

