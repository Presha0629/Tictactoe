import random
Choices=["a11","a12","a13","b11","b12","b13","c11","c12","c13"]
userList=[]
comList=[]
draw=True
while True:

    userChoice=input("mark your spot: ")
    if userChoice not in Choices:
        print("The item has already been chosen: ")
        continue
    for i in Choices:
        if i==userChoice:
          userList.append(i)
          Choices.remove(userChoice)
    print("Remaining choices after user have chosen: ", Choices)   
    if "a11" in userList and "a12" in userList and "a13" in userList:
        print("User wins")
        draw=False
        break
    elif "b11" in userList and "b12" in userList and "b13" in userList:
        print("User wins")
        draw=False
        break  
    elif "c11" in userList and "c12" in userList and "c13" in userList:
        print("User wins")
        draw=False
        break 
    elif "a11" in userList and "b11" in userList and "c11" in userList:
        print("User wins")
        draw=False
        break    
    elif "a12" in userList and "b12" in userList and "c12" in userList:
        print("User wins")
        draw=False
        break 
    elif "a13" in userList and "b13" in userList and "c13" in userList:
        print("User wins")
        draw=False
        break
    elif "a11" in userList and "b12" in userList and "c13" in userList:
        print("User wins")
        draw=False
        break
    elif "a13" in userList and "b12" in userList and "c11" in userList:
        print("User wins")
        draw=False
        break
                
                            
    if Choices==[]:
        print("All the options has been chosen")
        break

    computerChoice= random.choice(Choices)
    comList.append(computerChoice)
    print(computerChoice)
    Choices.remove(computerChoice)
    print("Choices after computer have chosen: ",Choices)

    if "a11" in comList and "a12" in comList and "a13" in comList:
        print("Computer wins")
        draw=False
        break
    elif "b11" in comList and "b12" in comList and "b13" in comList:
        print("Computer wins")
        draw=False
        break  
    elif "c11" in comList and "c12" in comList and "c13" in comList:
        print("Computer wins")
        draw=False
        break 
    elif "a11" in comList and "b11" in comList and "c11" in comList:
        print("Computer wins")
        draw=False
        break    
    elif "a12" in comList and "b12" in comList and "c12" in comList:
        print("Computer wins")
        draw=False
        break 
    elif "a13" in comList and "b13" in comList and "c13" in comList:
        print("Computer wins")
        draw=False
        break
    elif "a11" in comList and "b12" in comList and "c13" in comList:
        print("Computer wins")
        draw=False
        break
    elif "a13" in comList and "b12" in comList and "c11" in comList:
        print("Computer wins")
        draw=False
        break     

print(userList)
print(comList)
if draw==True:
    print("Draw")




    