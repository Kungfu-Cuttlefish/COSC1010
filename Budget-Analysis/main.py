#
# Syrus Freeman
# 2/16/2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Initialize variables 
total = 0
amount_over = 0
amount_left = 0

# Enter Budget
print ('Enter the budget for the month')
budget = int(input())

# Expenses
for day in range (1, 31) :
    print ('Enter the expenses for day', day)
    expenses = int(input())
    total += expenses
# Went for a 30 day month

if total > budget :
    total - budget = amount_over
    print ('You are over budget by', amount_over,)
if total < budget :
    budget - total = amount_left
    print ('You are under budget by', amount_left)