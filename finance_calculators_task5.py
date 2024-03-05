# This is an investment calculator and a home loan repayment calculator
"""TO add 
while True:
try:
user_input = float(input("Enter a numeric value greater than zero: "))
if 0<= user_input <=100:
break # Exit the loop if user input is valid
else:
print("Please enter a value greater than zero.")
except ValueError:
print("Invalid input. Please enter a numeric value.")
"""

import math

while True:
    # Display and request user to choose either calculator,Handle case sensitive and space error of user input
    calculator_choice = input('''
    investment - to calculate the amount of interest you''ll earn on your investment
    bond       - to calculate the amount you'll have to payon a home loan
                            
    Enter either 'investment' or 'bond' from the menu above to proceed:''').lower().replace(" ","")
     

    # Investment caculator branch:
    if calculator_choice == "investment":
        while True:
            try:
                deposit = float(input("Enter how much you want to deposit: "))
                if deposit < 0:
                     raise ValueError ("Input cannot be negative!") # Force jump to except block
                #Only the number of the interest rate should be entered — don’t worry about having to deal with the added ‘%’
                Interest_rate = float(input("Enter the yearly interest rate: "))
                if Interest_rate < 0:
                     raise ValueError ("input cannot be negative!") # Force jump to except block
                Invest_years = float(input("Enter how many years you want to invest: "))
                if Invest_years < 0:
                     raise ValueError ("Input cannot be negative!") # Force jump to except block
                break
            except ValueError: # Handle non-numeric and negative input 
                print("Not valid input, please only enter numbers! Try again!")
             
        Invest_type = input("Enter the investment type: simple or compound ")
        # Handle case sensitive and space error of user input
        Invest_type = Invest_type.lower()
        Invest_type = Invest_type.strip()
        # Simple interest type branch
        if Invest_type == "simple":
            # Simple rate investment formula: Total = Deposit * (1+interest rate * number of years)
            Simpleinvest_result = deposit * (1+Interest_rate/100 * Invest_years)
            print(round(Simpleinvest_result))
            
        # Compound interest type branch
        if Invest_type == "compound":
            # Compound rate investment formula: Total = Deposit * math.pow ((1+interest rate), number of years)
            Compoundinvest_result = deposit * math.pow((1+Interest_rate/100), Invest_years)
            print(round(Compoundinvest_result))
        

    # Bond caculator branch:
    elif calculator_choice == "bond":
        while True:
            try:
                House_value = float(input("Enter your house value: "))
                if House_value < 0:
                    raise ValueError ("Input cannot be negative!") # Force jump to except block
                #Only the number of the interest rate should be entered — don’t worry about having to deal with the added ‘%’
                Loan_rate = float(input("Enter your home loan annual interest rate: "))
                if Loan_rate < 0:
                    raise ValueError ("Input cannot be negative!") # Force jump to except block
                Loan_months = float(input("Enter your home loan terms in months: "))
                if Loan_months < 0:
                    raise ValueError ("Input cannot be negative!") # Force jump to except block
                # Caculate the loan monthly rate
                Loan_ratemonth = Loan_rate/100/12
                break
            except ValueError: # Handle non-numeric and negative input 
                print("Not valid input, please only enter numbers! Try again!")
        # Loan monthly payment formula: repayment = (monthly rate * deposit)/(1 - (1 + monthly rate)**(-number of months))
        Loanpayment_month = (Loan_ratemonth * House_value) / (1-(1+Loan_ratemonth)**(-Loan_months))
        print(round(Loanpayment_month))
        
    # Handle invalid input of caculator choice input
    else:
        print("Not valid choice, please enter again!")


