# The program determines if a customer is a target for a
# marketing campaign.  

zipCode = 48710
population = 17000
demoCode   = 1

isAtarget = False

# Determine customer is a target

if zipCode >= 48000 and zipCode <= 49999  and  \
    population >10000 and \
    (demoCode == 1  or demoCode == 3 or demoCode == 8):
    isAtarget = True
else:
    isAtarget = False


# Output results
print(isAtarget)
