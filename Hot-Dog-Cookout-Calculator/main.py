#
# Syrus Freeman
# 2/9/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Constants
HOT_DOGS_PER_PACKAGE = 10.0
BUNS_PER_PACKAGE = 8.0

#Local Variables
numAttending = 0   # The number of people attending
numPerPerson = 0   # The number of hot dogs and buns per person
total = 0          # The total number of hot dogs and buns needed
minDogs = 0        # The minimum number of packages of hot dogs
minBuns = 0        # The minimum number of packages of hot dog buns
dogsLeft = 0       # The number of hot dogs left over froma package
bunsLeft = 0       # The number of hot dog buns left over from a package

# number of people attending the cookout from the user.
numAttending = int(input('Enter the number of people attending the cookout: '))

# number of hot dogs per person from the user
numPerPerson = int(input('Enter the number of hot dogs per person: '))

# Calculate the total number of hot dogs and buns needed
total = numAttending * numPerPerson

# minimum number of packages of hot dogs needed
minDogs = total // HOT_DOGS_PER_PACKAGE

# number of people attending is large enough to require more than one package of hot dogs
if minDogs > 0:
    dogsLeft = total % HOT_DOGS_PER_PACKAGE
    # if there will be left overs add more dogs
    if dogsLeft != 0:
        minDogs += 1

else :
    minDogs = 1
dogsLeft = HOT_DOGS_PER_PACKAGE * minDogs - total

# minimum number of packages of hot dogs needed
minDogs = total // HOT_DOGS_PER_PACKAGE

# number of people attending is large enough to require more than one package of buns
if minBuns > 0:
    bunsLeft = total % BUNS_PER_PACKAGE
    # if there will be left overs add more buns
    if bunsLeft != 0:
        minBuns += 1

else :
    minBuns = 1
dogsLeft = BUNS_PER_PACKAGE * minBuns - total

print ('Minimum packages of buns needed: ', minBuns)

print ('Buns left over: ', bunsLeft)