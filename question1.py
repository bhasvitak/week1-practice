parking_hours = int(input("Enter the parking hours: "))

if parking_hours<=2:
    parking_charges = 30*parking_hours
elif parking_hours<=5:
    parking_charges = 25*parking_hours
else:
    parking_charges = 20*parking_hours

print(f"Parking Charges: {parking_charges} Rupees")
if parking_charges>150:
    print(f"Service Charges: 20 Rupees")
    print(f"Total Charges: {parking_charges+20} Rupees")
else:
    print(f"Service Charges: 0 Rupees")
    print(f"Total Charges: {parking_charges} Rupees")
