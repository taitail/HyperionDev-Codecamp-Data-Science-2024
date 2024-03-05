# Request user to input a number
# User enters "-1", program stop requesting user to enter a number,or keep requesting user input number
# Caculate the average of the numbers entered, excluding the -1

total = 0
count = 0

while True:
    # Request user input number
    user_input = input("Enter a number (or -1 to stop): ")
    try:
        number = float(user_input)
        if number == -1:
            break # User enters "-1", program stop
        total += number
        count += 1
    except ValueError: # Handle non-numeric input
        print("Please enter a valid number.")

if count > 0:
    average = round(total / count,2) # Caculate the average of number entered,round 2 digits
    print(f"The average of the numbers entered is {average}.")
else:
    print("No numbers were entered.")
