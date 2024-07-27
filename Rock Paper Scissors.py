import random
print("Welcome to the Game \n\nRules:\n 1. Rock vs Paper -> Paper Win's\n 2. Paper vs Scissors -> Scissors Win's\n 3. Rock vs Scissors -> Rock Win's")
print("\nLet's Play")
print("\nYour Choices\n 1.Rock\n 2.Paper\n 3.Scissors")
while True:
    choice=int(input("\nEnter Your Choice : "))
    while True:
        if (choice==1):
            choice_name="Rock"
            break
        elif(choice==2):
            choice_name="Paper"
            break
        elif(choice==3):
            choice_name="Scissors"
            break
        else:
            print("Wrong Choice! pls select correct choice")
            choice=int(input("\nEnter Your Choice : "))
    print("Your Choice is ",choice_name)
    print("\nNow Its Computer's Turn...")
    comp_choice=random.randint(1,3)
    if (comp_choice==1):
        comp_choice_name="Rock"        
    elif(comp_choice==2):
        comp_choice_name="Paper"    
    else:
        comp_choice_name="Scissors"
    print("Your Choice is ",comp_choice_name)
    if(comp_choice==choice):
        print("\nIt's a Draw")
    elif(comp_choice==1 and choice==2)or(comp_choice==2 and choice==3)or(comp_choice==3 and choice==1):
        print("\nYou Win's")
    else:
        print("\nComputer Win's")
    opt=input("\nDo You Want To Play Again!(Y/N):").strip().lower()
    if(opt!='y'):
        print("Thank You! For Playing")
        break
            