#operator overloading...

class InsurancePolicy:
    def __init__(self,policy_id,customer,coverage):
        self.policy_id=policy_id
        self.customer=customer
        self.coverage=coverage

    def __str__(self):
        return(
            f"Policy({self.policy_id}),"
            f"Customer({self.customer}),"
            f"Coverage({self.coverage})"
        )
    # + operator..
    def __add__(self,other):
        if isinstance(other,InsurancePolicy):   # this checks that is other a object of InsurancePolicy class.
            combined_coverage =( self.coverage + other.coverage)
            
            return InsurancePolicy("COMBINED",self.customer,combined_coverage)
        return NotImplemented
    
    # ==operator 
    def __eq__(self,other):
        if isinstance(other,InsurancePolicy):
            return self.policy_id==other.policy_id
        return NotImplemented
    # < operator
    def __lt__(self,other):
         if isinstance(other,InsurancePolicy):
             return self.coverage < other.coverage
         return NotImplemented
     # > operator 
    def __gt__(self,other):
        if isinstance(other,InsurancePolicy):
            return self.coverage > other.coverage 
        return NotImplemented
# now create objects
policy1 =InsurancePolicy( "POL1001","SAKSHI",100)
policy2=InsurancePolicy("POL1002","SOHAM",500)

print(policy1)
print(policy2)

print("/nCoombined Policy:")
combined=policy1+policy2
print(combined)
        
print("\nComparison:")
print("Same Policy:" ,policy1 ==policy2)
print("Policy1 < Policy2:",policy1<policy2)
print("Policy1 > Policy2:",policy1 >policy2)   
    