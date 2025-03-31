#
# Syrus Freeman
# 3/30/2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
import random
numbers = [0] * 7
numbers
[0, 0, 0, 0, 0, 0, 0]
for index in range (7):
    numbers [index] = random.randint (0, 9)

MAX_DIGITS = 7 
START = 0
END = 9

# main function
def main ():
    # create a list
    numbers = [0] * 7

    for index in range (MAX_DIGITS):
        numbers[index] = random.randint (START, END)
    
    print ('Here are your lottery numbers: ')
    for index in range (MAX_DIGITS):
        print (numbers [index], end='')
    print ()
main ()