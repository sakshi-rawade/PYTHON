# #reference count..

# import sys
# policy ={
#     "policy_id":"POL1001",
#     "customer":"SAKSHI RAWADE",
#     "coverage": 5000000
# }
# print(sys.getrefcount(policy))
# print("_-----------------------------------------------------------------------------------------------------")
# # gc module:- it interacts with cyclic garbage cycle
# import gc 
# collected =gc.collect()
# print("Objects collected:",collected)

# print(gc.get_threshold())
# print(gc.get_count())
# gc.enable()
#gc.disable

#TFL Insurance Demonstration
import gc 
class Customer:
    pass
class InsurancePolicy:
    pass

customer=Customer()
policy=InsurancePolicy()

customer.policy=policy
policy.customer=customer

print("Object created..")

del customer
del policy

print("References deleted..")

collected =gc.collect()
print("Garbage Collected:",collected)