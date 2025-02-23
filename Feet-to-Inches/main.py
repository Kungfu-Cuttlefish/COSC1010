#
# Syrus Freeman
# 2/23/2025
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
INCHES_PER_FOOT = 12
def main () :

    feet = int (input ('Enter a number of feet: '))

    print (feet, 'equals', feet_to_inches(feet), 'inches.')

def feet_to_inches (feet) : 
    return feet * INCHES_PER_FOOT

main ()