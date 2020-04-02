import random

r = random.randint(1,51)
print("Hey Aadit, Guess the number choosen by Computer")
x = int(input())
k = 0
while k==0:
    if x == r:
        print("============ Wow! Aadit You Chose the Correct Number ============")
        k = 1
    else:
        if x<r:
            print("============ AADIT, Dont give up. Your Answer is too low! Want to try again? Y/N ============")
            a = input()
            if a == 'N':
                k = 1
                print("System Guessed: " + str(r))
            elif a == 'Y':
                print("Great! Choose a new number")
                x = int(input())
            else:
                print("Sorry! Invalid Input")
             
        if x>r:
            print("============ AADIT, Dont give up. Your Answer is too High! Want to try again? Y/N ============")
            a = input()
            if a == 'N':
                k = 1
                print("System Guessed: " + str(r))    
            elif a == 'Y':
                print("Great Job AADIT! Choose a new number")
                x = int(input())
            else:
                print("Sorry! Invalid Input")