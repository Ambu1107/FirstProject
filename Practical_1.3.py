from datetime import datetime
def age(birthday):
    birth_year=int(birthday.split('-')[-1])
    current_year=datetime.now().year
    return current_year-birth_year
def salary(payment):
    salary=0.012*payment
    return salary
birthday=input("Enter a birthday:")
payment=float(input("Enter a payment:"))
age=age(birthday)
salary=salary(payment)
print(f"Age: {age}")
print(f"Salary in dollars: {salary:.2f}")