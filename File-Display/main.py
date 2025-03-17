#
# Syrus Freeman
# 3/16/2025
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Open the file.
myfile = open ('File-Display//numbers.txt', 'r')

# Read and display file's contents.
for line in myfile:
    number = int (line)
    print (number)

# Close the file.
myfile.close ()