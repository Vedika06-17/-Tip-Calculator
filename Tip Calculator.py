print("Welcome to the tip calculator ")
bill=int(input("What was the total bill?\nRs\t"))
tip=int(input("What tip would you like to give?10,12 or 15\n"))
people=int(input("How many people divide the bill?\n"))
tipp=tip/100
total_tip=tipp*bill
total=total_tip+bill
total_bill=total/people
ro=round(total_bill)
print(f"Bill for everyone is:{ro} ")