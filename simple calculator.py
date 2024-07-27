import string
print("Greetings! welcome")
print("simple calculator \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Divition \n 5.Exit")
opt='1'
while(opt!='5'):
    opt=input("choose your choice: ")
    if(opt.isnumeric()):
        if(opt>'0' and opt<='5'):
            if(opt=='5'):
                print("thank you,calculator closed!")
            else:
                a=int(input("enter first number :"))
                b=int(input("enter second number :")) 
                if(opt=='1'):
                    print(a+b)
                elif(opt=='2'):
                    print(a-b)
                elif(opt=='3'):
                    print(a*b)
                elif(opt=='4'):
                    print(a/b)
        else:
            print("choose option correctly")
    else:
            print ('enter correct option')
            