# 💰 Tip Calculator

## 📝 Overview

This project is a simple Tip Calculator written in Python. It allows users to calculate the total bill per person, including the tip percentage they choose to give.

## ⭐ Features

- 🧮 Calculates the total bill with a tip percentage.
- 👥 Splits the total bill evenly among a given number of people.
- 🔢 Uses Python's built-in `input()` function to collect user inputs.

## ⚙️ How It Works

The script follows these steps to calculate the tip and total bill per person:

1. **🖊️ User Input:**
   - The program prompts the user to input the total bill amount.
   - The user selects a tip percentage (10%, 12%, or 15%).
   - The user inputs the number of people to split the bill among.
2. **💲 Tip Calculation:**
   - The tip amount is calculated by multiplying the bill with the tip percentage.
   - The total bill is determined by adding the tip amount to the original bill.
3. **🔢 Per Person Bill Calculation:**
   - The total bill is divided equally among all individuals.
   - The final amount is rounded for better readability.
4. **🖥️ Display Output:**
   - The program prints the final amount each person has to pay.

## 🖥️ Code Explanation

```python
print("Welcome to the tip calculator ")
bill=int(input("What was the total bill?\nRs\t"))
tip=int(input("What tip would you like to give?10,12 or 15\n"))
people=int(input("How many people divide the bill?\n"))
```

- The user is welcomed to the tip calculator.
- The total bill, tip percentage, and number of people are collected as inputs from the user.

```python
tipp=tip/100
total_tip=tipp*bill
total=total_tip+bill
total_bill=total/people
ro=round(total_bill)
```

- The tip amount is calculated by converting the tip percentage into decimal form (`tip / 100`) and multiplying it by the total bill.
- The total amount to be paid (including the tip) is computed.
- The bill is split evenly among the number of people.
- The final amount per person is rounded to make it easier to read.

```python
print(f"Bill for everyone is:{ro} ")
```

- The final amount per person is displayed as output.

## ▶️ How to Run the Program

1. ✅ Ensure you have Python installed.
2. 📋 Copy and paste the script into a Python file (e.g., `tip_calculator.py`).
3. 🏃 Run the script using `python tip_calculator.py`.
4. ✍️ Follow the prompts to enter the bill amount, tip percentage, and number of people.
5. 💵 Get the final amount each person needs to pay.

## 📌 Example Output

```
Welcome to the tip calculator
What was the total bill?
Rs 1000
What tip would you like to give? 10, 12 or 15
12
How many people divide the bill?
4
Bill for everyone is: 280
```

## 🚀 Improvements

- 🎯 Allow users to enter custom tip percentages.
- 📉 Add an option to round up or down to the nearest decimal.
- 📊 Provide a breakdown of how much each person contributes to the tip.

## 🎯 Conclusion

This Python tip calculator is a simple yet useful tool for splitting bills and ensuring everyone pays their fair share. It efficiently calculates the total bill, including tips, and evenly distributes the cost among multiple individuals. 💵✨

