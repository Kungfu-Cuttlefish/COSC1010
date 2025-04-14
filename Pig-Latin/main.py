#
# Syrus Freeman
# 4/13/2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def main():
    # Get the sentance from the user and split the words apart
    words = str (input ("Please input the sentance you would like written in pig-latin: ")).split ()
    for word in words:
        # Move the first letter to the end of each word and add "ay" after the product
        print (word[1:] + word[0] + "ay", end = " ")
    #print again so the new sentance is on it's own line in the terminal
    print ()
# call main
main()
