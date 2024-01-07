#write a fucntion that returns the lesser of two given numbers .
#If both numbers are even,but
#returns the greater if one or both numbers are odd.

def lesser_number(a, b):
    if a % 2 == 0 and b % 2 == 0:
        # BOTH NUMBERS ARE EVEN!
        if a < b:
            result = a
        else:
            result = b
    else:
        # ONE OR BOTH NUMBERS ARE ODD!!
        if a > b:
            result = a
        else:
            result = b
    return result

print(lesser_number(2, 4))

print(lesser_number(2, 5))
    
    
