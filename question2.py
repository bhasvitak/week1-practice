name = input("Enter your name: ")
age = int(input("Enter your age: "))
tickets = int(input("Enter the no of tickets: "))

if age<12:
    price = 120
elif 12<=age<60:
    price = 200
else:
    price = 150
total=tickets*price
discount = 0
total1 = 0
if tickets >= 5:
    discount = 0.1*total
    total1=total-discount

print(f"Customer Name: {name}")
print(f"Ticket Price: {price}")
print(f"Number of Tickets: {tickets}")
print(f"Total Before Discount: {total}")
print(f"Discount: {discount}")
print(f"Final Amount: {total1}")