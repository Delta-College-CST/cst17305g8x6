# This program validates a floor number for a
# 19-story building with floors 1-20 (omitting floor 13).

# Input floor number
floor = int(input("Enter floor number: "))

# Validate to insure existent floor number
while floor < 1 or floor > 20 or floor == 13:
    print ("Nonexistent floor!")
    floor = int(input("Enter floor number: "))

# Output
print("Floor",floor,"is valid")
