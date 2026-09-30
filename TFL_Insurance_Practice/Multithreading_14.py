# #Multithreading..
# import threading
# import time

# def download_policy():
#     print("Downloading policy...")
#     time.sleep(3)
#     print("Policy downloaded")
    
# def send_email():
#     print("Sending email...")
#     time.sleep(2)
#     print("Email sent")
    
# t1=threading.Thread(target=download_policy)
# t2=threading.Thread(target=send_email)

# t1.start()   # start the execution of thread..
# t2.start()

# t1.join()   #main thread wait until this thread finishes
# t2.join()

# print("All tasks completed..")

#MultiProcessing
# from multiprocessing import Process
# def calculate():
#     total =0
    
#     for i in range(10_000_000):
#         total +=i 
#     print(total)
    
# if __name__ == "__main__":
#      p1=Process(target=calculate)
#      p2=Process(target=calculate)

#      p1.start()
#      p2.start()

#      p1.join()
#      p2.join()

# print("Completed..")

#Async Programming

import asyncio

async def download_policy():
    print("Downloading..")
    await asyncio.sleep(3)
    print("Downloaded..")
    
async def send_email():
    print("Sending email..")
    await asyncio.sleep(2)
    print("Email sent")

async def main():
    await asyncio.gather( download_policy(),send_email())
    
asyncio.run(main())