# #==============file open 
# with open("policies.json","r") as file:
#     data =file.read()

# #read json
# import json 

# with open("policies.json","r") as file:
#     policies =json.load(file)
# print(policies)    

#=============python to json 
# policy ={
#     "policy_number":"POL1003",
#     "customer_name":"broo",
#     "premium":18000,
#     "status":"Active"
# }
# import json
# with open("policies.json","w") as file:
#     json.dump(policy,file,indent=4)
#====================== #adding new policy 

# import json
# with open("policies.json","r") as file:
#     policies =json.load(file)
    
# new_policy ={
#     "policy_number":"POL1004",
#     "customer_name":"Manu",
#     "premium":20000,
#     "status":"Active"
# }
# policies.append(new_policy)

# with open("policies.json","w") as file:
#     json.dump(policies,file,indent=4)

#=============================================
# import json
# with open("policies.json","r") as file:
#     policies =json.load(file)
    
# new_policy ={
#     "policy_number":"POL1004",
#     "customer_name":"Manu",
#     "premium":20000,
#     "status":"Active"
# }
# # policies.append(new_policy)

# with open("policies.json","a") as file:
#     json.dump(new_policy,file,indent=4)

#=======================Find the policyy
# import json
# def find_policy(policy_number):
#     with open("policies.json","r") as file:
#         policies =json.load(file)
        
#     for policy in policies:
#         if policy["policy_number"]==policy_number:
#             return policy
#     return None 

# p=find_policy("POL1004")
# print(p)

#==========================file not found
# import json
# try:
#     with open("policie.json","r") as file:
#         policies=json.load(file)
# except FileNotFoundError:
#     print("Policy file does not exist.")
#     policies=[]

#========================= if json is corrupted
# import json
# try:
#     with open("policies.json","r") as file:
#         policies =json.load(file)
# except FileNotFoundError:
#     print("Policy file not found.")
#     policies=[]
# except json.JSONDecodeError:
#     print("Policy file contains invalid JSON.")
#     policies=[]

#============= Policy Repository 
import json
class PolicyRepository:
    def __init__(self,filename):
        self.filename =filename
    def get_all(self):
        try:
            with open(self.filename,"r") as file:
                return json.load(file)
        except FileNotFoundError():
            return []
        except json.JSONDecodeError:
            return []

repository =PolicyRepository("policies.json")
policies =repository.get_all()
print(policies)