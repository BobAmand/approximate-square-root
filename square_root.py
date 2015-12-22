'''
Python Code for Square Root
 assignment 1-Sep-2015
 revisited 22-Dec-2015
Goal: use recursion (function calling themselves)

'''
num = int(input("Enter a positive number: "))


def newtonest(num):
    return num ** 0.5   # num raised to power of (1/2)


def estimate(num):
    guess = num/3  # initial guess
    count = 0
    epsilon = 0.00001  # minimal difference between estimate and actual.
    sq_guess = ((num / guess) + guess)/2
    while abs(newtonest(num) - sq_guess) > epsilon:
        newguess = sq_guess
        sq_guess = ((num / newguess) + newguess)/2
        count += 1
    print("The square root of {} is {} with {} interations.".format(num,
                                                                    sq_guess,
                                                                    count))

estimate(num)
