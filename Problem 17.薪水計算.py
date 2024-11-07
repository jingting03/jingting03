hours_worked, hourly_wage = input().split()
hours_worked = int(hours_worked)   
hourly_wage = int(hourly_wage)   

salary = 0.0

if hours_worked <= 60:
    salary = hourly_wage * hours_worked
elif hours_worked <= 120:
    salary = hourly_wage * 60 + (hourly_wage * 1.33 * (hours_worked - 60))
else:
    salary = hourly_wage * 60 + (hourly_wage * 1.33 * 60) + (hourly_wage * 1.66 * (hours_worked - 120))

print(f"{salary:.1f}")
