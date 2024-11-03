import random
rc=random.randint(0,2)
user=int(input("Enter your Choice: "))
if(rc==user):   
    print("Your match is draw")
elif(rc==0 and user==1):
    print("User is the winner")
elif(rc==0 and user==2):
    print("System is the winner")
elif(rc==1 and user==0):
    print("Systewem is the winner")
elif(rc==1 and user==2):
    print("User is ṭhe winner")
elif(rc==2 and user==0):
    print("User is the winner")
elif(rc==2 and user==1):
    print("System  is the winner")
else:
    print("Give the correct input")
