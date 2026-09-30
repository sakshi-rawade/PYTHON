#Create event dispatcher 

class EventDispatcher:
    def __init__(self):
        self.handlers ={}
    def subscribe(self,event_name,handler):
        if event_name not in self.handlers:
            self.handlers[event_name]=[]
            
        self.handlers[event_name].append(handler)
    
    def publish(self,event_name ,data):
        print(f"\nEvent Published:{event_name}")
        for handler in self.handlers.get(event_name,[]):
            handler(data)

#Claim Submitted Event 
def validate_claim(data):
    print("Validating claim:",data["claim_id"])
    
    if data["amount"]<=0:
        print("Invalid claim amount..")
        return
    print("Claim Validation completed..")
def notify_customer(data):
    print("Sending claim acknowledgement to:",data["customer_email"])
    
def notify_claims_officer(data):
    print("Notifying claims officer about:",data["claim_id"])
    
def update_audit_log(data):
    print("Recording claim submission in audit log..")
    
#Register Handlers..
dispatcher =EventDispatcher()
dispatcher.subscribe("ClaimSubmitted",validate_claim)
dispatcher.subscribe("ClaimSubmitted",notify_customer)
dispatcher.subscribe("ClaimSubmitted",notify_claims_officer)
dispatcher.subscribe("ClaimSubmitted",update_audit_log)

#Publish the event..
claim={
    "claim_id":"CLM1001",
    "customer_name":"Sak",
    "customer_email":"sak@gmail.com",
    "amount":5000
}
dispatcher.publish("ClaimSubmitted",claim)

print("-----------------------------------------------------------------------------------------------------")

#callback()
def process_premium_payment(amount,callback):
    print("Processing premium payment:",amount)
    print("Payment Successful..")
    callback(amount)
def payment_confirmation(amount):
    print("Premium payment confirmed:",amount)
    
process_premium_payment(25000,payment_confirmation)

print("------------------------------------------------------------------------------------------------")

#Processing Multiple Insurance Claims
#using asyncio

import asyncio

async def process_claim(claim_id,delay):
    
    print(f"Started processsing claim:{claim_id}")
    # print("**************************************************************")
    await asyncio.sleep(delay)
    print(f"Completed processing claim:{claim_id}")
    
async def main():
    await asyncio.gather(
        process_claim("CLM1001",3),
        process_claim("CLM1002",2),
        process_claim("CLM1003",1)
    )
asyncio.run(main())

print("--------------------------------------------------------------------------------")

#GUI Event Handling..
#Insurance Event Handling........
#using tkinter
#calculator.. 

import tkinter as tk

def calculate_premium():
    
    sum_assured=float(entry.get())
    premium = sum_assured * 0.05
    result_label.config(text=f"Illustrative Premium: RS.{premium:.2f}")
    
window=tk.Tk()

window.title("TFL Insurance Premium Calculator..")
window.geometry("400x250")

label=tk.Label(window,text="Enter Sum Assured..")
label.pack(pady=10)

entry=tk.Entry(window)
entry.pack()

button=tk.Button(window,text="Calculate Premium",command=calculate_premium)

button.pack(pady=20)
result_label=tk.Label(window,text="")
result_label.pack()

window.mainloop()

     