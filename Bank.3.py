actnames = ["Micha"]
actbalances = [1,000]

check = False
while check == False:
        print("Welcome to First Financial Credit Union!")

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. List All Accounts")
        print("5. Add Account")
        print("6. Remove Account")
        
        action = input("What would you like to do today?:")
        # Funnest code to create. The .index fuction takes the exact acctount I would like to add money to and just adds it. Didn't take super long to make, and helped me code basically everything else in this program. 
        if action == "Deposit":
            actname = input("Which account would like to Deposit into?:")
            money = input("how much would you like to Deposit?:")
            money= int(money)
            index= actnames.index(actname)
            actbalances[index] = actbalances[index] + money
            print("Thank you for banking with First Financial Credit Union! Have a wonderful day!" )
            
    
            
        elif action == "Withdraw":
            actname = input("Which account would like to Withdraw from?:")
            money = input("How much would you like to Withdraw?:")
            money= int(money)
            index= actnames.index(actname)
            actbalances[index] = actbalances[index] - money
            print("Thank you for banking with First Financial Credit Union! Have a wonderful day!" )
            
            
            
            # This was the most confusing code I had to put together. This lets me make a transfer from one account to another by using the .index fuction to pull the exact postion of the account I would like to transfer
            # from and to from the list that I created 
        elif action == "Transfer":
            actname = input("Which account would like to Transfer from?:")
            actname2 = input("Which account would like to Transfer to?:")
            money = input("how much would you like to Transfer?:")
            money= int(money)
            index= actnames.index(actname)
            index2 = actnames.index(actname2)
            actbalances[index] = actbalances[index] - money
            actbalances[index2] = actbalances[index2] + money
            print("Thank you for banking with First Financial Credit Union! Have a wonderful day!" )
            
        
            #The quickest code to make, took like 10 seconds to figure out, not a whole lot going on here, literallyt just printing everything in my list.
        elif action == "List All Accounts":
            print(len(actnames))
            
            
            
        elif action == "Add Account":
          actname = input("Which account would like to Add?:")
          actnames.append(actname)
          actbalances.append(0)
          
          
          
          # This was also pretty confusing.The .pop fuction allows me to remove the element from the exact postion in my list while also remvoing the balnce, something .remove would not do.  
        elif action == "Remove Account":
            actname = input("Which account would like to Remove?:")
            index= actnames.index(actname)
            actnames.pop(index) 
            actbalances.pop(index)
            print("Thank you for banking with First Financial Credit Union! Have a wonderful day!" )
            
            
            
        elif action == "quit":
            check = True
    











