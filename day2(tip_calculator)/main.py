print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

new_total_bill = total_bill * (tip/100)
total_bill_tip = total_bill + new_total_bill
final_bill = total_bill_tip/no_of_people
# rounded_final_bill = round(final_bill,2)
rounded_final_bill = "{:.2f}".format(final_bill)
print(f"Each person should pay: ${rounded_final_bill}")

