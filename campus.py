
# Campus Event Financial Planning

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input event expenses
venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transport cost per participant: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected participants: "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))

# Validate inputs
if (min(venue, equipment, catering, transport, certificate,
        registration_fee, sponsorship) < 0 or participants < 0):
    print("Invalid input! Values cannot be negative.")

else:
    # Calculate fixed and variable costs
    fixed_cost = venue + equipment
    variable_cost = catering + transport + certificate

    total_variable_cost = variable_cost * participants
    total_cost = fixed_cost + total_variable_cost

    # Calculate income
    participant_income = registration_fee * participants
    total_income = participant_income + sponsorship

    # Calculate shortfall or surplus
    difference = total_income - total_cost

    # Minimum registrations needed to break even
    contribution_per_person = registration_fee - variable_cost

    print("\n===== EVENT FINANCIAL REPORT =====")
    print("Fixed Costs: Rs.", round(fixed_cost, 2))
    print("Variable Cost per Participant: Rs.",
          round(variable_cost, 2))
    print("Total Variable Costs: Rs.",
          round(total_variable_cost, 2))
    print("Total Event Cost: Rs.", round(total_cost, 2))
    print("Participant Contributions: Rs.",
          round(participant_income, 2))
    print("Sponsorship: Rs.", round(sponsorship, 2))
    print("Total Available Income: Rs.", round(total_income, 2))

    if difference < 0:
        print("Financial Shortfall: Rs.", round(-difference, 2))
    else:
        print("Financial Surplus: Rs.", round(difference, 2))

    if contribution_per_person > 0:
        remaining_fixed_cost = max(0, fixed_cost - sponsorship)
        break_even = max(
            0,
            int(remaining_fixed_cost / contribution_per_person)
            + (1 if remaining_fixed_cost % contribution_per_person > 0
               else 0)
        )

        print("Minimum Registrations to Break Even:", break_even)

        if participants < break_even:
            print("Warning: More registrations are needed.")
        else:
            print("Event can break even with expected registrations.")

    else:
        if fixed_cost <= sponsorship:
            print("Break-even achieved through sponsorship.")
        else:
            print("Break-even is impossible at the current fee.")
            print("Increase the registration fee or sponsorship.")
