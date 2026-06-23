# Power Consumption Calculator

A Python application that calculates household appliance energy consumption, estimates monthly electricity costs, and exports reports to CSV format.

## Features

- Add multiple appliances
- Prevent duplicate entries
- Calculate daily energy consumption
- Calculate monthly energy consumption
- Estimate monthly electricity cost
- Sort appliances by energy usage
- Export reports to CSV
- Generate timestamped reports
- Input validation

## Technologies Used

- Python
- CSV Module
- Datetime Module

## Sample Input
### Sample Input

```
Appliance Name: Refrigerator
Power: 150
Hours Used: 24

Appliance Name: Television
Power: 120
Hours Used: 5

Appliance Name: Laptop
Power: 65
Hours Used: 8

Appliance Name: Ceiling Fan
Power: 80
Hours Used: 10

Appliance Name: Electric Kettle
Power: 2000
Hours Used: 0.5

Appliance Name: LED Light
Power: 12
Hours Used: 6

done

Electricity cost: 14
```

### Sample Output

```
----------------------------------------------------------------------------------------------------
Appliance           Power(W)            Hours Used          Energy(kWh)         
----------------------------------------------------------------------------------------------------
Refrigerator        150.00              24.00               3.60                
Electric Kettle     2000.00             0.50                1.00                
Ceiling Fan         80.00               10.00               0.80                
Television          120.00              5.00                0.60                
Laptop              65.00               8.00                0.52                
Led Light           12.00               6.00                0.07                
----------------------------------------------------------------------------------------------------
Total daily energy consumption(in kWh)                                          6.59
Total monthly energy consumption(in kWh)                                        197.76
Total monthly electricity cost(in ETB)                                          2768.64
----------------------------------------------------------------------------------------------------

Report saved successfully to Appliance_Report.csv
```
### Console input

![Console Input] (<img width="1913" height="1043" alt="Screenshot 2026-06-23 090428" src="https://github.com/user-attachments/assets/13330f82-9300-45dc-8b87-661bf86962d7" />)

### Console Output

![Console Output] (<img width="1411" height="1116" alt="Screenshot 2026-06-23 090443" src="https://github.com/user-attachments/assets/def181ad-7226-4cdb-bf9d-01fedfe5ad92" />)

### CSV Report

![CSV Report](<img width="1912" height="1122" alt="Screenshot 2026-06-23 090557" src="https://github.com/user-attachments/assets/2db0e7ff-dc46-452b-97d3-401699e5493c" />)

## How to Run

```bash
python power_consumption_calculator.py
```

## Author

**Firdews Hailu**  
Electrical Power and Control Engineering Student  
Adama Science and Technology University
