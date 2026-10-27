
# Hospital Billing and Patient Classification

patients = []

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nEnter details for Patient", i + 1)

    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    consultation = float(input("Enter consultation charge: "))
    diagnostic = float(input("Enter diagnostic charge: "))
    treatment = float(input("Enter treatment charge: "))
    payment = float(input("Enter amount paid: "))
    senior = input("Is patient a senior citizen? (yes/no): ").lower()

    # Validate billing constraints
    if age < 0 or min(consultation, diagnostic, treatment, payment) < 0:
        print("Invalid input! Values cannot be negative.")
        continue

    total = consultation + diagnostic + treatment

    # Apply concessions
    concession = 0

    if senior == "yes":
        concession = total * 0.10
    elif total >= 10000:
        concession = total * 0.05

    final_bill = total - concession

    # Validate payment
    if payment > final_bill:
        print("Excess payment detected. Please check the amount.")
        continue

    balance = final_bill - payment

    # Patient classification
    if balance == 0:
        status = "Fully Paid"
    elif payment > 0:
        status = "Partially Paid"
    else:
        status = "Unpaid"

    patients.append({
        "name": name,
        "total": total,
        "concession": concession,
        "final_bill": final_bill,
        "payment": payment,
        "balance": balance,
        "status": status
    })

# Display billing report
print("\n========== HOSPITAL BILLING REPORT ==========")

for p in patients:
    print("\nPatient Name:", p["name"])
    print("Total Charges: Rs.", round(p["total"], 2))
    print("Concession: Rs.", round(p["concession"], 2))
    print("Final Bill: Rs.", round(p["final_bill"], 2))
    print("Amount Paid: Rs.", round(p["payment"], 2))
    print("Balance Due: Rs.", round(p["balance"], 2))
    print("Patient Classification:", p["status"])

print("\nTotal valid patient bills:", len(patients))
