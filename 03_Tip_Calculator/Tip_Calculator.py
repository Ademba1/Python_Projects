### TIP Calculator

print("Welcome to the Tip Calcuator\n")

bill = float(input("What was the total bill? $"))

percentage_tip = int(input("What percentage Tip would you like to give? 10, 12, or 15?"))

No_of_people = int(input("How many people to split the bill?"))

total_bill = bill * (1+ percentage_tip /100)

amount_to_pay = "{:.2f}".format(total_bill/No_of_people)

print(f"Each person should pay: ${amount_to_pay}")
