import time
import math


def hypcalc():
    print("\nThis calculates the hypotenuse of a right-angled triangle")
    time.sleep(0.5)
    print("\nEnter one of the sides (cm)")
    side1 = float(input())
    print("\nEnter the other side (cm)")
    side2 = float(input())

    side1sqrd = math.pow(side1, 2)

    side2sqrd = math.pow(side2, 2)

    hypsqrd = (side1sqrd + side2sqrd)

    hyp = math.sqrt(hypsqrd)

    print("\nThe hypotenuse is " + str(float(hyp)) + " cm")

    

def rightangled():
    print("\nPlease enter one of the sides (cm)")
    side1 = float(input())

    print("\nPlease enter another side (cm)")
    side2 = float(input())

    print("\nPlease enter the final side (cm)")
    side3 = float(input())

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



def spareside():
    print("Please enter the hypotenuse (cm)")
    side1 = int(input())
    print("Please enter the other side (cm)")
    side2 = int(input())

    sides = [side1, side2]
    sides.sort()

    hyp = sides[1]
    other = sides[0]

    hypsqrd = math.pow(hyp, 2)
    othersqrd = math.pow(other, 2)

    sparesqrd = (hypsqrd - othersqrd)

    spare = math.sqrt(sparesqrd)

    print("\nThe spare side is " + str(float(spare)) + " cm")

print("What would you like to run?")
print("1. Hypotenuse calculator")
print("2. Right-angle verifier")
print("3. Remaining side calculator\n")
choice = input()

if choice == "1":
    hypcalc()

elif choice == "2":
    rightangled()

elif choice == "3":
    spareside()

