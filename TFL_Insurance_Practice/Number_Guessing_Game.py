import random 
secret_number =random.randint(1,100)
attempts =0

print("---Number Guessing Game ---")
print(" I have selected a number between 1 and 100.")

while True:
    guess =int(input("Enter the number selected:"))
    attempts +=1
    
    if guess <secret_number:
        print("Too Low ! Try Again..")
    elif guess >secret_number:
        print("Too High! Try Again..")
    else:
        print("Veryyyyyyyyy Gooooodddd")
        print("You guessed the correct number.")
        
        print("Attempts:",attempts)
        break
    
    
print("Show the random number generate:", secret_number)
