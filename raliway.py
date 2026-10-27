
print("===== RAILWAY FARE AND RESERVATION CALCULATOR =====")

n = int(input("Enter number of passengers: "))
distance = float(input("Enter travel distance in km: "))

total_fare = 0

for i in range(1, n + 1):
    print("\nPassenger", i)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))

    print("Travel Classes:")
    print("1. Sleeper - Rs. 1 per km")
    print("2. AC 3 Tier - Rs. 2 per km")
    print("3. AC 2 Tier - Rs. 3 per km")

    choice = int(input("Choose travel class (1-3): "))

    if choice == 1:
        class_name = "Sleeper"
        rate = 1
    elif choice == 2:
        class_name = "AC 3 Tier"
        rate = 2
    elif choice == 3:
        class_name = "AC 2 Tier"
        rate = 3
    else:
        print("Invalid class! Using Sleeper class.")
        class_name = "Sleeper"
        rate = 1

    # Calculate basic fare
    basic_fare = distance * rate

    # Age-based concession
    concession = 0

    if age < 5:
        concession = basic_fare
    elif age >= 60:
        concession = basic_fare * 0.20

    fare_after_concession = basic_fare - concession

    # Reservation fee
    reservation_fee = 40

    # Total fare
    fare = fare_after_concession + reservation_fee

    print("\n----- Passenger Fare Details -----")
    print("Name:", name)
    print("Age:", age)
    print("Travel Class:", class_name)
    print("Distance:", distance, "km")
    print("Basic Fare: Rs.", round(basic_fare, 2))
    print("Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Total Fare: Rs.", round(fare, 2))

    # Cancellation
    cancel = input("Cancel ticket? (yes/no): ").lower()

    if cancel == "yes":
        penalty = fare * 0.25
        refund = fare - penalty

        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))
        fare = 0

    total_fare += fare

print("\n===== FINAL SUMMARY =====")
print("Total Amount Payable: Rs.", round(total_fare, 2))
print("Thank you for using the Railway Calculator!")

