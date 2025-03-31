#
# Syrus Freeman
# 3/30/2025
# Exception Handling Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

total = 0
try:
    # Open the file
    myfile = open ('Exception-Handling//numbers.txt', 'r')

    # Read and average the file's contents
    number_list = myfile.readlines()

    for number in number_list:
        total = total + float (number)

    myfile.close ()
    print (total / len(number_list))
except IOError:
    print ('An IOError occured.')

except ValueError:
    print ('A ValueError occured')

