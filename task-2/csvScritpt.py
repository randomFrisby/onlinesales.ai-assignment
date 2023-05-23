import csv

def generate_top_departments(csv_file):
    # Read data from the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Calculate average monthly salary for each department
    departments = {}
    for row in data:
        dept_name = row['DEPT_NAME']
        salary = float(row['MONTHLY_SALARY'])

        if dept_name in departments:
            departments[dept_name].append(salary)
        else:
            departments[dept_name] = [salary]

    # Calculate average monthly salary for each department
    avg_salaries = {}
    for dept_name, salaries in departments.items():
        avg_salary = sum(salaries) / len(salaries)
        avg_salaries[dept_name] = avg_salary

    # Sort departments based on average salary
    sorted_departments = sorted(avg_salaries.items(), key=lambda x: x[1], reverse=True)

    # Print top 3 departments along with their names and average monthly salary
    for dept, avg_salary in sorted_departments[:3]:
        print("DEPT_NAME:", dept)
        print("AVG_MONTHLY_SALARY (USD):", avg_salary)
        print()

# Usage example
csv_file = 'departments.csv'  # Replace with the actual path to your CSV file
generate_top_departments(csv_file)
