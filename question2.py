name = input("Enter customer name: ")
age = int(input("Enter age: "))
tickets = int(input("Enter number of tickets: "))

if age < 12:
    price = 120
elif age < 60:
    price = 200
else:
    price = 150

total = price * tickets

if tickets >= 5:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

print()
print("Customer Name:", name)
print("Ticket Price: ₹", price, sep="")
print("Number of Tickets:", tickets)
print("Total Before Discount: ₹", total, sep="")
print("Discount: ₹", discount, sep="")
print("Final Amount: ₹", final_amount, sep="")