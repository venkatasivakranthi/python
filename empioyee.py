
# Employee Payroll and Deduction Analysis

# Get employee details
name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

# Get salary details
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

# Calculate gross salary
gross_salary = basic + allowances + overtime + incentives

# Calculate progressive tax deduction
if gross_salary <= 20000:
    tax = 0
elif gross_salary <= 40000:
    tax = (gross_salary - 20000) * 0.10
elif gross_salary <= 60000:
    tax = 20000 * 0.10 + (gross_salary - 40000) * 0.20
else:
    tax = 20000 * 0.10 + 20000 * 0.20 + (gross_salary - 60000) * 0.30

# Other deductions
pf = basic * 0.12
total_deductions = tax + pf

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display salary statement
print("\n====================================")
print("        EMPLOYEE SALARY STATEMENT")
print("====================================")
print("Employee Name :", name)
print("Employee ID   :", emp_id)
print("------------------------------------")
print(f"Basic Salary  : Rs. {basic:.2f}")
print(f"Allowances    : Rs. {allowances:.2f}")
print(f"Overtime Pay  : Rs. {overtime:.2f}")
print(f"Incentives    : Rs. {incentives:.2f}")
print("------------------------------------")
print(f"Gross Salary  : Rs. {gross_salary:.2f}")
print(f"Income Tax    : Rs. {tax:.2f}")
print(f"PF Deduction  : Rs. {pf:.2f}")
print(f"Total Deduct. : Rs. {total_deductions:.2f}")
print("------------------------------------")
print(f"NET SALARY    : Rs. {net_salary:.2f}")
print("====================================")
