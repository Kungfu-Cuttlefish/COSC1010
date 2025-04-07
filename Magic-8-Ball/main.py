#
# Syrus Freeman
# 4/6/2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random
# list of responses
responses = [
    "Yes, of course!",
    "Without a doubt, yes.",
    "You can count on it.",
    "For sure!",
    "Ask me later.",
    "I'm not sure.",
    "I can't tell you right now.",
    "I will tell you after my nap.",
    "No way!",
    "I don't think so.",
    "Without a doubt, no.",
    "The answer is clearly NO.",
]

while True:
    question = input ("Ask your question. (or type quit to exit)")
    # End the loop when needed
    if question.lower() == "quit":
        print ("Goodbye! ")
        break
    # Print response
    print ("Magic 8-ball says:", random.choice(responses))