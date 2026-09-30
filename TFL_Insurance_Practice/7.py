#Exception Handling.

# try and except
# try:
#     premium =int (input ("Enter premium amount:"))
#     print("Premium:",premium)

# except:
#     print("Invalid premium amount.")
    
# print("------------------------------------")

# proper try except block
# try: 
#     premium =int(input("Enter premium:"))
    
# except ValueError:
#     print("Please enter valid numeric premium.")

# print("-----------------------------------------")

# #premium validation
# try: 
#     premium =float (input("Enter annual premium:"))
    
#     if premium <=0:
#         raise ValueError("Premium must be greater than zero.")
#      print("Premium accepted:",premium)
        
# except ValueError as ex:
#     print("Invalid premium:",ex)
    
# #multiple exceptions
# try:
#     age=int(input("Enter age:"))
# except ValueError:
#     print("Age must be a number.")
    
# except TypeError:
#     print("Invalid data type.")
    
# #if everything works then else condition will excute 
# try:
#     premium =float(input("Enter premium:"))
# except ValueError:
#     print("Invalid Premium.")
# else:
#     print("Premium accepted.")
    
# #finally.
# #TFLInsurance Payment
# def pay_premium(amount):
#     try:
#         amount=float(amount)
#         if amount <=0:
#             raise ValueError("Payment amount  must be positive.")
#         print("Processing payment...")
#         print("Payment Successsful..")
#     except ValueError as ex:
#         print("Payment failed:",ex)
#     finally:
#         print("Payment operation completed.")
        
# pay_premium(-58)

# #policy not found
# policies ={
#     "POL1001": "Life Insurance",
#     "POL1002": "Health Insurance"
    
# }

# def get_policy(policy_number):
#     if policy_number not in policies:
#         raise KeyError(
#             f"Policy {policy_number} does not exist."
#         )
#     return policies[policy_number]
# try:

#     policy = get_policy("POL1002")
#     print(policy)

# except KeyError as ex:

#     print("Policy error:", ex)
    
# #Custom Exceptions
class PolicyNotFoundException(Exception):
    pass

policies ={
    "POL1001": "Life Insurance",
    "POL1002": "Health Insurance"
    
}

def get_policy(policy_number):

    if policy_number not in policies:
        raise PolicyNotFoundException(
            f"Policy {policy_number} was not found."
        )

    return policies[policy_number]

try:

    policy = get_policy("POL1002")
    print(policy)

except PolicyNotFoundException as ex:

    print(ex)