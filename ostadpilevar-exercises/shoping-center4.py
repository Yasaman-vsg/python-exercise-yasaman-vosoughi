print("welcome yas shop")

while True:
    x=input("do you want to buy?")
    c=x.lower()
    if c=="yes":
         print("here you are")
         break
    elif c=="no" :
         print("goodbye")    
         break
    elif c==" yes":
         print("incorrect answer")
         
    else :
        print(" answer yes or no")
         
