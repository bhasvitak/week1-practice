values = [10, 10, 20, 20, 20, 30, 10, 10, 40]
print(f"Original List:\n{values}")
for i in range(len(values)-1, 0, -1):
    if values[i] == values[i-1]:
        values.pop(i)

print(f"Result:\n{values}")