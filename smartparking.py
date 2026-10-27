
from datetime import datetime, timedelta
import math

def calculate_parking_fee():
    print("===== SMART PARKING FEE MANAGEMENT =====")

    vehicle = input("Enter vehicle type (Bike/Car/Truck): ").strip().lower()

    rates = {
        "bike": 20,
        "car": 50,
        "truck": 100
    }

    if vehicle not in rates:
        print("Invalid vehicle type!")
        return

    entry = input("Enter entry time (YYYY-MM-DD HH:MM): ").strip()
    exit_time = input("Enter exit time (YYYY-MM-DD HH:MM): ").strip()

    try:
        entry_time = datetime.strptime(entry, "%Y-%m-%d %H:%M")
        exit_time = datetime.strptime(exit_time, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid time format! Please use YYYY-MM-DD HH:MM.")
        return

    if exit_time <= entry_time:
        print("Error: Exit time must be after entry time.")
        return

    duration = exit_time - entry_time
    total_minutes = duration.total_seconds() / 60
    hours = math.ceil(total_minutes / 60)

    # Parking charges per hour
    rate = rates[vehicle]
    days = math.ceil(total_minutes / 1440)

    # Calculate hourly charges with a daily maximum
    daily_limit = {
        "bike": 150,
        "car": 300,
        "truck": 600
    }

    fee = 0

    for day in range(days):
        remaining_hours = hours - (day * 24)
        parked_hours = min(24, remaining_hours)
        fee += min(parked_hours * rate, daily_limit[vehicle])

    # Overnight parking penalty
    overnight = entry_time.date() != exit_time.date()
    overnight_fee = 100 if overnight else 0

    # Penalty for parking longer than 7 days
    penalty = 500 if duration.days >= 7 else 0

    total_fee = fee + overnight_fee + penalty

    print("\n===== PARKING RECEIPT =====")
    print("Vehicle Type     :", vehicle.title())
    print("Entry Time       :", entry_time)
    print("Exit Time        :", exit_time)
    print("Parking Duration :", duration)
    print("Parking Charges  : Rs.", fee)
    print("Overnight Fee    : Rs.", overnight_fee)
    print("Penalty          : Rs.", penalty)
    print("Total Amount     : Rs.", total_fee)
    print("===========================")

calculate_parking_fee()
