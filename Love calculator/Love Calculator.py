print("Welcome to Love Calculator")

yourName = input("Enter Your Full Name : ")
partnerName = input("Enter Your Partner's ' Name :")

import random 
score = random.randrange(1,101) 

if(score<30):
    print(f"Your Love Score is {score}, and install tinder")
elif(score>=30 and score<=70):
    print(f"Your Love Score is {score}, and you are normal couple")
else:
    print("Your Love Score is ",score,"and you are a romantic couple")
