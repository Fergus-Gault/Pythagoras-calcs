import time
import math

#Use again feature
def playagain():
    while True:
        try:
            print("Would you like to use this again? (Y/N)")
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
            print("You didn't enter a valid response, please try again")
            time.sleep(0.5)
            continue

        try:
            print("\nEnter the second side (cm)")
            side2 = float(input())

        except ValueError:
            print("You didn't enter a valid response, please try again")
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


#Second calculator
def rightangled():
    print("This figures out if the triangle is right-angled based on the numbers entered")
    time.sleep(0.5)
    while True:
        try:
            print("\nPlease enter the first side (cm)")
            side1 = float(input())

        except ValueError:
            print("\nYou didn't enter a valid response, please try again")
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

    shortsqrd = math.pow(short, 2)
    longsqrd = math.pow(long, 2)

    ans = (shortsqrd + longsqrd)

    if hypsqrd == ans:
        print("This is a right-angled triangle")

    else:
        print("This is not a right-angled triangle")

    playagain()

#Third calculator
def spareside():
    print("This calculates the missing side of a triangle")
    time.sleep(0.5)
    print("\nPlease enter the hypotenuse (cm)")
    side1 = float(input())

    print("Please enter the other side (cm)")
    side2 = float(input())

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

def anglecalc():

    print("This calculates the angle of a triangle")
    time.sleep(0.5)
    formulas = ["Sin", "Cos", "Tan"]
    while True:
        try:
            print("Please enter the formula you would like to use: Sin, Cos or Tan")
            formula = input().lower()
        except ValueError:
            print("Please enter a valid response")
            formula = input().lower()

        if formula == "sin":
            while True:
                try:
                    print("\nPlease enter the opposite (cm)")
                    opp = float(input())

                except ValueError:
                    print("\nYou did not enter a valid response, please try again")
                    time.sleep(0.5)
                    continue


                try:
                    print("\nPlease enter the hypotenuse (cm)")
                    hyp = float(input())

                except ValueError:
                    print("You did not enter a valid response, please try again")
                    time.sleep(0.5)
                    continue

                else:
                    break


            #Maths formula
            order = [opp, hyp]
            order.sort()

            opp = order[0]
            hyp = order[1]
            
            ans1 = (opp/hyp)

            ans = math.degrees(math.asin(ans1))


            print("The angle you are looking for is " + str(ans) + "°\n")

            playagain()


        elif formula == "cos":

            while True:
                try:
                    print("\nPlease enter the adjacent (cm)")
                    adj = float(input())

                except ValueError:
                    print("\nYou did not enter a valid response, please try again")
                    time.sleep(0.5)
                    continue

                try:
                    print("\nPlease enter the hypotenuse")
                    hyp = float(input())

                except ValueError:
                    print("\nYou did not enter a valid response, please try again")
                    time.sleep(0.5)
                    continue

                else:
                    break


            #Maths formula
            order = [adj, hyp]
            order.sort()

            adj = order[0]
            hyp = order[1]

            ans1 = (adj/hyp)

            ans = math.degrees(math.acos(ans1))

            print("The angle you are looking for is " + str(ans) + "°\n")

            playagain()

        elif formula == "tan":
            while True:
                try:
                    print("\nPlease enter the opposite (cm)")
                    opp = float(input())

                except ValueError:
                    print("\nYou did not enter a valid response, please try again")
                    time.sleep(0.5)
                    continue

                try:
                    print("\nPlease enter the adjacent (cm)")
                    adj = float(input())

                except ValueError:
                    print("You did not enter a valid response, please try again")
                    time.sleep(0.5)
                    continue

                else:
                    break


            #Maths formula
            order = [adj, opp]
            order.sort()

            adj = order[0]
            opp = order[1]

            ans1 = (opp/adj)

            ans = math.degrees(math.atan(ans1))

            print("The angle you are looking for is " + str(ans) + "°\n")

            playagain()





def calculator():
    print("This is a regular calculator")
    time.sleep(0.5)
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y


    
    
    print("Select operator:")
    print("+")
    print("-")
    print("*")
    print("/\n")

    choice = input()
    choicelist = ["+", "-", "*", "/"]
    while choice not in choicelist:
        print("Select operator:")
        print("+")
        print("-")
        print("*")
        print("/\n")

        choice = input()
        choicelist = ["+", "-", "*", "/"]

    while True:        
        try:
            print("Please enter the first number\n")
            num1 = int(input())
        except ValueError:
            print("Please enter a valid input\n")
            continue

        else:
            break
        
        
    while True:
        try:
            print("Please enter the second number\n")
            num2 = int(input())
        except ValueError:
            print("Please enter a valid input\n")
            continue

        else:
            break
        

    if choice == "+":
        print(num1, "+" , num2, "=", add(num1, num2))

    elif choice == "-":
        print(num1, "-" , num2, "=", subtract(num1, num2))

    elif choice == "*":
        print(num1, "*" , num2, "=", multiply(num1, num2))

    elif choice == "/":
        print(num1, "/" , num2, "=", divide(num1, num2))

    else:
        print("Invalid input")

    playagain()
        
    

#Menu
def menu():

    print("What would you like to run?")
    print("---------------------------------")
    print("| 1. Hypotenuse calculator      |")
    print("| 2. Right-angle verifier       |")
    print("| 3. Remaining side calculator  |")
    print("| 4. Angle calculator           |")
    print("| 5. Regular calculator         |")
    print("---------------------------------")

    choice = input()

    if choice == "1":
        hypcalc()

    elif choice == "2":
        rightangled()

    elif choice == "3":
        spareside()

    elif choice == "4":
        anglecalc()

    elif choice == "5":
        calculator()

    choicelist = ["1", "2", "3", "4", "5"]
    while choice not in choicelist:

        print("What would you like to run?")
        print("---------------------------------")
        print("| 1. Hypotenuse calculator      |")
        print("| 2. Right-angle verifier       |")
        print("| 3. Remaining side calculator  |")
        print("| 4. Angle calculator           |")
        print("| 5. Regular calculator         |")
        print("---------------------------------")

        choice = input()

        if choice == "1":
            hypcalc()

        elif choice == "2":
            rightangled()

        elif choice == "3":
            spareside()

        elif choice == "4":
            anglecalc()

        elif choice == "5":
            calculator()

        playagain()

menu()
