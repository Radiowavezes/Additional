employee_list = []
while True:
    name = input('Enter the name: ')
    salary = int(input('Enter the salary: '))
    employee_list.append(name)
    employee_list.append(salary)
    do_continue = input('Do you want to continue? y/n ')
    if do_continue == 'n':
        break
max_salary = 0
for i in range(1, len(employee_list), 2):
    if employee_list[i] > max_salary:
        max_salary = employee_list[i]
for i in range(1, len(employee_list), 2):
    if employee_list[i] == max_salary:
        print(employee_list[i - 1], '-', employee_list[i], end='', sep=' ')
