#untrustworthy banks website :)

excon = False

humanlist = ["Teague,Sebas,Prestone,Andrew,x æ a xii"] #bank account list
cashlist = ["$439,$-253,$0,$5000000,$490000000000"] #bank account balances

while excon == False:
    print ("hello human, what would you like to do?")
    print ("deposit into an account")
    print ("withdraw from an account")
    print ("transfer money between accounts")
    print ("add an account")
    print ("remove an account")
    print ("list balanes(s)")
    print ("quit")
    system = input ("system accessed.")
    if system == quit: #exit condition
        print ("thank you for using untrustworthy banks! come again.")
    excon == True 