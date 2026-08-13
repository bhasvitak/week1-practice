employee = ("Arjun", "Developer", 45000, 3)
name , role, salary, experience = employee
annual_salary = salary*12
if experience<2:
    bonus = (5/100)*annual_salary
elif 2<=experience<=5:
    bonus = (10/100)*annual_salary
elif experience>5:
    bonus = (15/100)*annual_salary
    
print(f"Employee Name: {name}")
print(f"Designation: {role}")
print(f"Experience: {experience}")
print(f"Monthly Salary: {salary}")
print(f"Annual Salary: {annual_salary}")
print(f"Bonus: {bonus}")
print(f"Total Annual Compensation: {annual_salary+bonus}")
