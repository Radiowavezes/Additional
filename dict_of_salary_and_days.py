def get_key_salary(n, my_dict):
    for i, j in my_dict.items():
        if j[0] == n:
            return i

def get_key_days(n, my_dict):
    for i, j in my_dict.items():
        if j[0] == n:
            return i


names = ['Barry', 'Allan', 'Dylon', 'Casey', 'Isaac']
salary = [1250, 1200, 1300, 1500, 1350]
missed_days = [0, 5, 10, 1, 3]
employees_dict = {}
for i, j, k in zip(names, salary, missed_days):
    employees_dict[i] = [j, k]
min_salary = min(salary)
min_missed_days = min(missed_days)
print(get_key_salary('The less salary has', min_salary, employees_dict))
print(get_key_days('The less ammount of days is missed by', min_missed_days, employees_dict))
