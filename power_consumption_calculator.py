import csv
from datetime import datetime

appliance = {}
def add_appliance(name,power,hour_used):
    if name in appliance:
        print(f"{name} already exists with power and time of {appliance[name]}.")
        print(f"Did u want to update the power? (yes/no)")
        choice = input().lower()
        if choice == 'yes':
            appliance[name] = {"power": power,"time": hour_used,"energy": (power* hour_used) / 1000}
            print(f"{name} updated to {power}W.")
        else:
            print(f"{name} remains at {appliance[name]}W.")
        return
    appliance[name] = {"power": power,"time": hour_used,"energy": (power* hour_used) / 1000}
    
##########
def calculate_daily_consumption(appliance):
    total_daily_energy = 0
    for name, data in appliance.items():
        total_daily_energy += data["energy"]
    return total_daily_energy

##########
def calculate_monthly_consumption(appliance):
    total_monthly_energy = 0
    for name, data in appliance.items():
        total_monthly_energy += (data["energy"]*30)
    return total_monthly_energy

##########
def calculate_electricity_cost_per_month(appliance, cost):
    total_monthly_energy = calculate_monthly_consumption(appliance)
    total_cost = total_monthly_energy * cost
    return total_cost
    
##########
def print_report(appliance,cost):
    if not appliance:
        print("No appliances entered.")
        return
    sorted_appliances = sorted(appliance.items(),key=lambda item: item[1]['energy'],reverse=True)

    print("-"*100)
    print(f"{'Appliance':<20}{'Power(W)':<20}{'Hours Used':<20}{'Energy(kWh)':<20}")
    print("-"*100)
    for name, data in sorted_appliances:
        print(f"{name:<20}{data['power']:<20.2f}{data['time']:<20.2f}{data['energy']:<20.2f}")
    print("-"*100)
    print(f"{'Total daily energy consumption(in kWh)':<80}{calculate_daily_consumption(appliance):.2f}")
    print(f"{'Total monthly energy consumption(in kWh)':<80}{calculate_monthly_consumption(appliance):.2f}")
    print(f"{'Total monthly electricity cost(in ETB)':<80}{calculate_electricity_cost_per_month(appliance, cost):.2f}")
    print("-"*100)

##########
def export_to_csv(appliance,cost):
    sorted_appliances = sorted(appliance.items(),key=lambda item: item[1]['energy'],reverse=True)
    fields = ['Appliance', 'Power(W)', 'Hours Used', 'Energy(kWh)']
    with open("Appliance_Report.csv", "w", newline="") as wdcsv:
        csv_writer = csv.DictWriter(wdcsv, fieldnames=fields)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        csv_writer.writerow({"Appliance": f"Generated On: {current_time}"})
        csv_writer.writerow({})
        csv_writer.writeheader()
        csv_writer.writerows([{"Appliance": name, "Power(W)": data["power"], "Hours Used": data["time"], "Energy(kWh)": data["energy"]} for name, data in sorted_appliances])
        csv_writer.writerow({})
        csv_writer.writerow({"Appliance": "Total Daily Energy", "Energy(kWh)": calculate_daily_consumption(appliance)})
        csv_writer.writerow({"Appliance": "Total Monthly Energy", "Energy(kWh)": f"{calculate_monthly_consumption(appliance):.2f}"})
        csv_writer.writerow({"Appliance": "Total Monthly Cost (ETB)", "Energy(kWh)": calculate_electricity_cost_per_month(appliance, cost)})

###### Main program

print(f"Welcome to the Power Consumption Calculator!\n")
print(f"To procced please enter the appliance name, its power consumption in Watt and the time used in a day(in hours)")
while True:
    print(f"Enter appliance name, or done to finish: ")
    name = input().strip().title()
    if name.lower() == "done":
        break
    else:
        print(f"Enter power consumtion in Watt: ")
        while True:
            try:
                power = float(input())
                if power <= 0:
                    print("Power must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        print(f"Enter time used in a day (in hours): ")
        while True:
            try:
                hour_used = float(input())
                if hour_used <= 0 or hour_used > 24:
                    print("Time must be greater than 0 and less than or equal to 24.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        add_appliance(name, power,hour_used)
while True:
    try:
        cost = float(input("Enter electricity cost(in ETB per kWh):"))
        if cost <= 0:
            print("cost must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")
print_report(appliance,cost)
export_to_csv(appliance,cost)
print("\nReport saved successfully to Appliance_Report.csv")
