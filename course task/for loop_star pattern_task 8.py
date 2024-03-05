# Output the star pattern shown below, using an if-else statement in combination with a single for loop 
"""
*
**
***
****
*****
****
***
**
*
"""
star=""
# Star gets an additional * for lines 1 through 5, and for lines 6 through 9, it loses one * at each step by slicing off the last character.
for line in range(1,10):
    if line <=5:
        star += "*"
    else:
        star = star[:-1]
    print(star)
    