

#garbage collection 
# class Customer:
#     def __init__(self,name):
#         self.name=name
    
#     def __str__(self):
#         return self.name
# customer1=Customer("Soham")
# customer2 =customer1

# print(customer1)
# print(customer2)

# customer1=None    # we observe here that when is set customer1 to None, customer2 still stores the same value
#                    # which earlier it was pointing to. i.e soham      
# print(customer2)

#Circular References
import gc

class Customer:
    def __init__(self,name):
        self.name=name
        self.policy=None
class Policy:
    def __init__(self,number):
        self.number=number
        self.customer =None
customer=Customer("Ravi")
policy=Policy("P1001")

customer.policy=policy
policy.customer=customer

customer=None
policy=None

print("Requesting GC...")

collected =gc.collect()

print("Collected:",collected)