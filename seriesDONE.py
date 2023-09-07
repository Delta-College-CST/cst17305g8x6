# This program sums a arithmetic sequence

# Input
start     = int(input("Enter start value: "))
increment = int(input("Enter increment: "))

NUMBER_TERMS = 100

# Generate terms
sum = 0
term = start
for num in range (0,NUMBER_TERMS):
    sum  = sum + term
    term = term + increment

print("Sum: ",sum)
    
