# #oops concepts 

class Policy:
    def __init__(self, policy_number, customer_name,
                 policy_type, premium):

        self.policy_number = policy_number
        self.customer_name = customer_name
        self.policy_type = policy_type
        self.premium = premium

    def display(self):
        print(self.policy_number)
        print(self.customer_name)
        print(self.policy_type)
        print(self.premium)


policy1 = Policy("POL1001", "SAKSHIII", "Life", 25000)

policy2 = Policy("POL1002", "SOHAM", "CAR", 50000)

policy1.display()


print("-------------------------------------------------------------------------------")

#Encapsulation 
class Claim:
    def __init__(self,claim_id,amount):
        self.__amount=amount
        
    def get_amount(self):
        return self.__amount
    
    def update_amount(self,amount):
        if amount > 0:
            self.__amount=amount
print("-----------------------------------------------------")
#Inheritance 
class Employee:
    def __init__(self,employee_id,name):
        self.employee_id =employee_id
        self.name=name
        
    def display(self):
        print(self.employee_id ,self.name)
        
#agent class inherit the employee class.      
class Agent(Employee):
    def sell_policy(self):
        print("Selling insurance policy..")

#claimsofficer inherite the employee class
class ClaimsOfficer(Employee):
    def process_claim(self):
        print("Processing Claim..")       
        
print("-----------------------------------------------------")

#Polymorphism 

#calculate_premium: same function but diffrent behaviour.
class LifePolicy:
    def calculate_premium(self):
        return 25000
    
class HealthPolicy :
    def calculate_premium (self):
        return 18000
    
class MotorPolicy:
    def calculate_premium(self):
        return 12000
    
policies =[
    LifePolicy(),
    HealthPolicy(),
    MotorPolicy()
]

for policy in policies :
    print(policy.calculate_premium())

 
