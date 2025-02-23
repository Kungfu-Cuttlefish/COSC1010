#
# Syrus Freeman
# 2/23/2025
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
CONVERSION_FACTOR = 0.6214

def main () :
    # Get the distance in km
    kilometers = float (input ('Enter a distance in kilometers: '))

    # Display the distance converted into miles.
    show_miles (kilometers)

def show_miles (km) :
    # Calculate miles

    miles = km * CONVERSION_FACTOR

    print (km, 'kilometers equals', miles, 'miles.')

main ()
# Couldn't figure out how to get rid of trailing 9s on any number >1 (10 gives an answer of 6.213999)