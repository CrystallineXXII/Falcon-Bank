d={1000:[1234,50000,"Steve"],2000:[1767,25000,"leo"],3000:[4567,30000,"joh-n"]}
l={1:8,2:13,3:4,4:6}
s={1:7,2:9,3:12,4:15,5:21}
adm = 123456
password=654321
while True:
    x=int(input("Enter account number: "))
    if x in d:
        print("Welcome", d[x][2])
        print("Menu","1. Withdraw","2. Transfer","3. Loan","4. Invest","5.Quit",sep="\n")
        ch=int(input("Enter choice: "))
        if ch==1:
            print("WITHDRAW",end="\n")
            p=int(input("Enter pin: "))
            if p==d[x][0]:
                print("Balance: ", d[x][1])
                a=int(input("Enter withdrawal amount: "))
                if a>d[x][1]:
                    print("Insufficient funds")
                else:
                    d[x][1]=d[x][1]-a
                    print("Balance: ", d[x][1])
            else:
                print("Incorrect pin")
        elif ch==2:
            print("TRANSFER",end="\n")
            p=int(input("Enter pin: "))
            if p==d[x][0]:
                print("Balance: ", d[x][1])
                a=int(input("Enter transfer amount: "))
                if a>d[x][1]:
                    print("Insufficient funds")
                else:
                    n=int(input("Enter reciever account number: "))
                    q=int(input("Enter reciever account pin: "))
                    if q==d[n][0]:
                        if n in d:
                            d[x][1]=d[x][1]-a
                            d[n][1]+=a
                            print(x,"account balance: ",d[x][1])
                            print(n,"account balance: ",d[n][1])
                        else:
                            print("Incorrect pin")
            else:
                print("Incorrect pin")
        elif ch==3:
            print("LOAN",end="\n")
            p=int(input("Enter pin: "))
            if p==d[x][0]:
                print("Balance: ",d[x][1])
                print("Choose loan","1. Home loan","2. Car loan","3. Gold loan","4. Student loan",sep="\n")
                c=int(input("Enter choice: "))
                if c==1:
                    print("Interest rate: ",l[c],"%")
                    y=int(input("Enter loan amount: "))
                    z=int(input("Enter loan duration (in months): "))
                    print("Projected value: ",y+(y*(l[c]/100)*(z/12)))
                    j=input("Confirm loan (y/n): ")
                    if j=="y":
                        d[x][1]+=y
                        print("Loan confirmed")
                        print("Balance: ",d[x][1])
                    else:
                        print("Loan cancelled")
                elif c==2:
                    print("Interest rate: ",l[c],"%")
                    y=int(input("Enter loan amount: "))
                    z=int(input("Enter loan duration (in months): "))
                    print("Projected value: ",y+(y*(l[c]/100)*(z/12)))
                    j=input("Confirm loan (y/n): ")
                    if j=="y":
                        d[x][1]+=y
                        print("Loan confirmed")
                        print("Balance: ",d[x][1])
                    else:
                        print("Loan cancelled")
                elif c==3:
                    print("Interest rate: ",l[1],"%")
                    y=int(input("Enter loan amount: "))
                    z=int(input("Enter loan duration (in months): "))
                    print("Projected value: ",y+(y*(l[1]/100)*(z/12)))
                    j=input("Confirm loan (y/n): ")
                    if j=="y":
                        d[x][1]+=y
                        print("Loan confirmed")
                        print("Balance: ",d[x][1])
                    else:
                        print("Loan cancelled")
                elif c==4:
                    print("Interest rate: ",l[1],"%")
                    y=int(input("Enter loan amount: "))
                    z=int(input("Enter loan duration (in months): "))
                    print("Projected value: ",y+(y*(l[1]/100)*(z/12)))
                    j=input("Confirm loan (y/n): ")
                    if j=="y":
                        d[x][1]+=y
                        print("Loan confirmed")
                        print("Balance: ",d[x][1])
                    else:
                        print("Loan cancelled")
                else:
                    print("Invalid choice")
            else:
                print("Incorrect pin")
        elif ch==4:
            print("INVEST",end="\n")
            p=int(input("Enter pin: "))
            if p==d[x][0]:
                print("Balance: ",d[x][1])
                print("Investmen plans","1. 1 Year plan","2. 2 Year plan","3. 5 Year plan","4. 7 Year plan","5. 10 Year plan",sep="\n")
                c=int(input("Enter choice: "))
                if c==1:
                    print("Interest rate: ",s[c],"%")
                    y=int(input("Enter Investment amount: "))
                    print("Projected value: ",y+(y*(s[c]/100)))
                    j=input("Confirm investment (y/n): ")
                    if j=="y":
                        if y>d[x][1]:
                            print("Insufficient funds")
                        else:
                            d[x][1]=d[x][1]-y
                            print("Investment confirmed")
                            print("Balance: ",d[x][1])
                    else:
                        print("Investment cancelled")
                elif c==2:
                    print("Interest rate: ",s[c],"%")
                    y=int(input("Enter Investment amount: "))
                    print("Projected value: ",y+(y*(s[c]/100)))
                    j=input("Confirm investment (y/n): ")
                    if j=="y":
                        if y>d[x][1]:
                            print("Insufficient funds")
                        else:
                            d[x][1]=d[x][1]-y
                            print("Investment confirmed")
                            print("Balance: ",d[x][1])
                    else:
                        print("Investment cancelled")
                elif c==3:
                    print("Interest rate: ",s[c],"%")
                    y=int(input("Enter Investment amount: "))
                    print("Projected value: ",y+(y*(s[c]/100)))
                    j=input("Confirm investment (y/n): ")
                    if j=="y":
                        if y>d[x][1]:
                            print("Insufficient funds")
                        else:
                            d[x][1]=d[x][1]-y
                            print("Investment confirmed")
                            print("Balance: ",d[x][1])
                    else:
                        print("Investment cancelled")
                elif c==4:
                    print("Interest rate: ",s[c],"%")
                    y=int(input("Enter Investment amount: "))
                    print("Projected value: ",y+(y*(s[c]/100)))
                    j=input("Confirm investment (y/n): ")
                    if j=="y":
                        if y>d[x][1]:
                            print("Insufficient funds")
                        else:
                            d[x][1]=d[x][1]-y
                            print("Investment confirmed")
                            print("Balance: ",d[x][1])
                    else:
                        print("Investment cancelled")
                elif c==5:
                    print("Interest rate: ",s[c],"%")
                    y=int(input("Enter Investment amount: "))
                    print("Projected value: ",y+(y*(s[c]/100)))
                    j=input("Confirm investment (y/n): ")
                    if j=="y":
                        if y>d[x][1]:
                            print("Insufficient funds")
                        else:
                            d[x][1]=d[x][1]-y
                            print("Investment confirmed")
                            print("Balance: ",d[x][1])
                    else:
                        print("Investment cancelled")
                else:
                    print("Invalid choice")
            else:
                print("Incorrect pin")
        elif ch==5:
            break
        else:
            print("Invalid choice")
    elif x==adm:
        k=int(input("Enter password:"))
        if k==password:
            while True:
                print('''              EDIT
                        1.Admin no & paswword
                        2.Existing accounts
                        3.Intrest on Loans
                        4.Intrest on investments
                        5.Quit''')
                ch=int(input('Enter choice:'))
                if ch==5:
                    break
                elif ch==4:
                    while True:
                        print('''
                           Intrest on Investments
                                  1.1 year
                                  2.2 year
                                  3.5 year
                                  4.7 year
                                  5.10 year
                                  6.Quit''')
                        ch=int(input("Enter choice: "))
                        if ch == 1:
                            b = int(input("Enter new interest rate:"))
                            l[1]= b
                            print("New interest rate:",l[1],'%')
                        elif ch == 2:
                            b = int(input("Enter new interest rate:"))
                            l[2]= b
                            print("New interest rate:",l[2],'%')
                        elif ch == 3:
                            b = int(input("Enter new interest rate:"))
                            l[3] = b
                            print("New interest rate:",l[3],'%')
                        elif ch == 4:
                            b = int(input("Enter new interest rate:"))
                            l[4]= b
                            print("New interest rate:",l[4],'%')
                        elif ch==5:
                            b = int(input("Enter new interest rate:"))
                            l[5]= b
                            print("New interest rate:",l[5],'%')
                        elif ch==6:
                            break
                        else:
                            print("Invalid choice")
                elif ch==3:
                    while True:
                        print('''Interest on Loans
                                   1. Home Loan
                                   2.Car Loan
                                   3.Gold Loan
                                   4.Student Loan
                                   5.Quit''')
                        ch=int(input("Enter choice: "))
                        if ch == 1:
                            b = int(input("Enter new interest rate:"))
                            l[1] = b
                            print("New interest rate:",l[1],'%')
                        elif ch == 2:
                            b = int(input("Enter new interest rate:"))
                            l[2] = b
                            print("New interest rate:",l[2],'%')
                        elif ch == 3:
                            b = int(input("Enter new interest rate:"))
                            l[3]= b
                            print("New interest rate:",l[3],'%')
                        elif ch == 4:
                            b = int(input("Enter new interest rate:"))
                            l[4] = b
                            print("New interest rate:",l[4],'%')
                        elif ch==5:
                            break
                        else:
                            print("Invalid choice")
                elif ch==1:
                    while True:
                        print('''
                        1.Admin no
                        2.Admin password
                        3.Quit''')
                        ch=int(input("Enter choice:"))
                        if ch==1:
                            adm=int(input("Enter new admin no:"))
                            print("Your new admin no is:",adm)
                        elif ch==2:
                            password = int(input("Enter new admin password:"))
                            print("Your new admin password is:" ,password)
                        elif ch==3:
                            break
                        else:
                            print("Invalid choice")
                elif ch==2:
                    print('''
                             1. Delete existing account
                             2. Add new Account
                             3. Quit''')
                    ch=int(input("Enter choice: "))
                    if ch==1:
                        i=int(input("Enter account no:"))
                        del(d[i])
                        print(d)
                    elif ch==2:
                        k=int(input('Enter account no:'))
                        z=int(input("Account pin:"))
                        j=input("Enter name:")
                        y=int(input("Enter acc balance:"))
                        d[k]=[z,y,j]
                        print(d)
                    elif ch==3:
                        break
                    else:
                            print("Invalid choice")
                else:
                            print("Invalid choice")
else:
    print("Account not found")


