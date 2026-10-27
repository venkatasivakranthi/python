
n = int(input("Enter number of vehicles: "))
distance = float(input("Enter journey distance (km): "))
reserve_percent = float(input("Enter reserve fuel percentage: "))

vehicles = []

for i in range(n):
    print("\nVehicle", i + 1)

    name = input("Enter vehicle name: ")
    mileage = float(input("Enter mileage (km/l): "))
    fuel_price = float(input("Enter fuel price per litre: "))
    available_fuel = float(input("Enter available fuel (litres): "))

    if mileage <= 0 or fuel_price < 0 or available_fuel < 0:
        print("Invalid vehicle details!")
        continue

    fuel_needed = distance / mileage
    reserve = fuel_needed * reserve_percent / 100
    total_fuel = fuel_needed + reserve
    cost = total_fuel * fuel_price

    feasible = available_fuel >= total_fuel

    vehicles.append({
        "name": name,
        "fuel": fuel_needed,
        "reserve": reserve,
        "total": total_fuel,
        "cost": cost,
        "feasible": feasible
    })

print("\n--- Fuel Consumption Report ---")

for v in vehicles:
    print("\nVehicle:", v["name"])
    print("Fuel required:", round(v["fuel"], 2), "litres")
    print("Reserve fuel:", round(v["reserve"], 2), "litres")
    print("Total fuel needed:", round(v["total"], 2), "litres")
    print("Journey cost: Rs.", round(v["cost"], 2))
    print("Status:", "Feasible" if v["feasible"] else "Not feasible")

feasible_vehicles = [v for v in vehicles if v["feasible"]]

if feasible_vehicles:
    best = min(feasible_vehicles, key=lambda v: v["cost"])
    print("\nLowest-cost feasible vehicle:", best["name"])
    print("Minimum journey cost: Rs.", round(best["cost"], 2))
else:
    print("\nNo vehicle has sufficient fuel for the journey.")
