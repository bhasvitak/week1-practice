n = int(input("Enter the number: "))
evens = 0
odds = 0
for i in range(1,11):
    if n*i %2 != 0:
        s = "Odd"
        odds+=1
    else:
        s= "Even"
        evens+=1
    print(f"{n} x {i} = {n*i} - {s}")

print(f"Even Result: {evens}")
print(f"Odd Result: {odds}")