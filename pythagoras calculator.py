import time
import math


#Play again feature
def playagain():
        while True:
            try:
                print("\nWould you like to use this again? (Y/N)")
                useAgain = input().lower()
                if useAgain == "y":
                    menu()

                elif useAgain == "n":
                    exit()

            except ValueError:
                print("\nWould you like to use this again? (Y/N)")
                useAgain == input()
                continue


#The first calculator
def hypcalc():
    print("\nThis calculates the hypotenuse of a right-angled triangle")
    time.sleep(0.5)
    while True:
        try:
            print("\nEnter the first side (cm)")
            side1 = float(input())

        except ValueError:
            print("You didn't enter a valid resonse, please try again")
            time.sleep(0.5)
            continue
        
        try:
            print("\nEnter the second side (cm)")
            side2 = float(input())
            
        except ValueError:
            print("You didn't enter a valid resonse, please try again")
            time.sleep(0.5)
            continue
        else:
            break

    #Maths formula    

    side1sqrd = math.pow(side1, 2)

    side2sqrd = math.pow(side2, 2)

    hypsqrd = (side1sqrd + side2sqrd)

    hyp = math.sqrt(hypsqrd)

    print("\nThe hypotenuse is " + str(float(hyp)) + " cm")

    playagain()


#Second Calculator
def rightangled():
    print("This figures out if the triangle is right-angled based on the numbers entered")
    time.sleep(0.5)
    while True:
        try:
            print("\nPlease enter the first side (cm)")
            side1 = float(input())

        except ValueError:
            print("You didn't enter a valid response, please try again")
            time.sleep(0.5)
            continue
        

        try:
            print("\nPlease enter the second side (cm)")
            side2 = float(input())
            
        except ValueError:
            print("You didn't enter a valid response, please try again")
            time.sleep(0.5)
            continue
        

        try:
            print("\nPlease enter the third side (cm)")
            side3 = float(input())

        except ValueError:
            print("You didn't enter a valid response, please try again")
            time.sleep(0.5)
            continue

        else:
            break

    #Maths formula
    sides = [side1, side2, side3]
    sides.sort()

    hyp = sides[2]

    hypsqrd = (hyp * hyp)

    short = sides[0]
    long = sides[1]

    shortsqrd = (short * short)
    longsqrd = (long * long)

    ans = (shortsqrd + longsqrd)


    if hypsqrd == ans:
        print("This is a right-angled triangle")

    else:
        print("This is not a right-angled triangle")

    playagain()

#Third Calculator
def spareside():
    print("This calculated the missing side of a triangle")
    time.sleep(0.5)
    print("\nPlease enter the hypotenuse (cm)")
    side1 = int(input())
    print("\nPlease enter the other side (cm)")
    side2 = int(input())

    sides = [side1, side2]
    sides.sort()

    hyp = sides[1]
    other = sides[0]

    #Maths formula
    hypsqrd = math.pow(hyp, 2)
    othersqrd = math.pow(other, 2)

    sparesqrd = (hypsqrd - othersqrd)

    spare = math.sqrt(sparesqrd)

    print("\nThe spare side is " + str(float(spare)) + " cm")

    playagain()

#Menu
def menu():

    

    print("What would you like to run?")
    print("---------------------------------")
    print("| 1. Hypotenuse calculator      |")
    print("| 2. Right-angle verifier       |")
    print("| 3. Remaining side calculator  |")
    print("---------------------------------\n")

    choice = input()

    if choice == "1":
        hypcalc()

    elif choice == "2":
        rightangled()

    elif choice == "3":
        spareside()
            
    choicelist = ["1", "2", "3"]
    while choice not in choicelist:

        
        print("What would you like to run?")
        print("---------------------------------")
        print("| 1. Hypotenuse calculator      |")
        print("| 2. Right-angle verifier       |")
        print("| 3. Remaining side calculator  |")
        print("---------------------------------\n")
        
        choice = input()

        if choice == "1":
            hypcalc()

        elif choice == "2":
            rightangled()

        elif choice == "3":
            spareside()
    playagain()
    
menu()  
