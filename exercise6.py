import random
life=5
if __name__ == "__main__":
    
    user_point=0
    computer_point=0
    i=10
    while True:
        print(f"\t\t\t\t\t\t\t\t\tlife ={life}")
        l1 = ['Snake','Gun','Water']
        l2 = []
        print("\t\t\t\tPress key to chose  ")
        print("\t\t\t\t0. Snake")
        print("\t\t\t\t1. Gun")
        print("\t\t\t\t2. Water")
        print("\t\t\t\t3. exit")
        n = int(input("\t\t\t\tEnter key"))
        if n ==1 or n == 0 or n == 2:
           chose=l1.pop(n)
        elif n == 3:
            exit()
        else:
            print("\n invalid choice \n try again")
            continue
        a,b=l1  #value unpack
        l2.append(a)
        l2.append(b)
        print("\t\t\t\tnow computer chance")
        c=random.choice(l2)
        if chose == 'Snake' and c == 'Water':
           print("you win")
           print(f"you chose {chose}  and computer chose {c}")
           user_point+=1
        elif chose == 'Snake' and c == 'Gun':
           print("computer win")
           print(f"you chose {chose}  and computer chose {c}")
           computer_point+=1
        elif chose == 'Gun' and c == 'Water':
            print("Computer win")
            print(f"you chose {chose}  and computer chose {c}")
            computer_point+=1
        elif chose == 'Gun' and c == 'Snake':
            print("You win")
            print(f"you chose {chose}  and computer chose {c}")
            user_point+=1
        elif chose == 'Water' and c == 'Gun':
            print("you win")
            print(f"you chose {chose}  and computer chose {c}")
            user_point+=1
        elif chose == 'Water' and c == 'Snake':
            print("computer win")
            print(f"you chose {chose}  and computer chose {c}")
            computer_point+=1
        life -= 1
        if life == 0:
            break
    if user_point > computer_point:
         print("******************************************* user_win****************************************")
         print(f"user_point {user_point}  and computer point {computer_point}")
    elif user_point < computer_point:
        print("******************************************** computer_win*************************************")
        print(f"user_point {user_point}  and computer point {computer_point}")
    else:
        print("******************************************* dwar *********************************************")
        print(f"user_point {user_point}  and computer point {computer_point}")
