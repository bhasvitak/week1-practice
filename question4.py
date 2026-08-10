text = input("Enter text: ")

upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0
other_count = 0

for ch in text:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch == " ":
        space_count += 1
    else:
        other_count += 1

print()
print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Other Characters:", other_count)