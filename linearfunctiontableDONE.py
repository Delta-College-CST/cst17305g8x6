# This program creates a table of (x,y) values for
# a linear function in the form: y = mx + b

# Collect input function    
m = float(input("For function y = mx + b, enter m: "))
b = float(input("For function y = mx + b, enter b: "))

# Enter parameters for table generation
start     = int(input("Enter table starting x: "))
end       = int(input("Enter table ending x: "))
increment = int(input("Enter table x-increment: ")) 

print()
print("  y =",m,"x +",b)
print("  ===============")
print("    x       y")
for x in range(start,end,increment):
    y = m * x + b
    print("%6.1f  %6.1f" % (x,y))  



