#
# Syrus Freeman
# 3/16/2025
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

total = 0
# Open the file
myfile = open ('Average-of-Numbers//numbers.txt', 'r')

# Read and average the file's contents
number_list = myfile.readlines()

for number in number_list:
    total = total + float (number)

myfile.close ()
print (total / len(number_list))