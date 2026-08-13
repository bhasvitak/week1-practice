expenses = [250, 1200, 450, 800, 150, 2000, 350]
total = sum(expenses)
average = total/len(expenses)
highest = max(expenses)
lowest = min(expenses)
above_500 = 0
below_500 = 0
for i in expenses:
    if i > 500:
        above_500+=1
    else:
        below_500+=1
print(f"Total Expense: {total}")
print(f"Average Expense: {average}")
print(f"Highest Expense: {highest}")
print(f"Lowest Expense: {lowest}")
print(f"Number of Expenses Above ₹500: {above_500}")
print(f"Number of Expenses Below or Equal to ₹500: {below_500}")

print("Expenses Above Average: ")
for i in expenses:
    if i>average:
        print(i)