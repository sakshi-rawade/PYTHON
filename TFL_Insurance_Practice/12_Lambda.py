#Lambda Function..
# square=lambda x: x*x
# print(square(3))

# #calculate discount 
# calculate_discount =lambda premium :premium *0.90
# print(calculate_discount(50000))

#tfl insurance policies 
policies =[
    { "policy_id":"POL1001","customer":"Sakshi","premium":25000,"coverage":1000},
    { "policy_id":"POL1002","customer":"Rohit","premium":50000,"coverage":5000},
    {"policy_id":"POL1003","customer":"Sanket","premium":28000,"coverage":7000},
    {"policy_id":"POL1004","customer":"Tanvi","premium":78000,"coverage":8000},   
]

#map() function..
# discounted =list(map(lambda p:{ **p,"discouted_premium":p["premium"] * 0.90},policies))
# print(discounted)

#filter() function 
# high_coverage=list(filter(lambda p: p["coverage"] > 5000,policies))
# print(high_coverage)

#sorted() function..
# sorted_policies =sorted(policies,key=lambda p:p["premium"],reverse =True)
# print(sorted_policies)