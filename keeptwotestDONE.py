# This program receives 3 test scores and writes the
# sum of the highest 2 tests.

# Input two numbers
test1 = int(input("Enter Test 1 score: "))
test2 = int(input("Enter Test 2 score: "))
test3 = int(input("Enter Test 3 score: "))

# Determine the sum of the highest two test scores
if test1 > test3 and test2 > test3:
    sum = test1 + test2
if test1 > test2 and test3 > test2:
    sum = test1 + test3
if test2 > test1 and test3 > test1:
    sum = test2 + test3

# Output results
print("Sum of hightest two tests: ",sum)
