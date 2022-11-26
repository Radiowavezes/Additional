import random
import time

#2
def template(first_name, last_name):
    return f'Hello, {first_name} {last_name}!'

#3
def convert(num: float) -> float:
    return round(num, 2) if int(num) != float(num) else int(num)
# print(convert(34.0))
# print(convert(22.32131))
# print(convert(58.60125))

#4
list_of_strings = ['price', 'hello', 'price', 'from', 'price']
price_capitalize = [i.upper() if i == 'price' else i for i in list_of_strings ]
# print(price_capitalize)

#5
def divider(any_list: list, num:int) -> list:
    
    section = len(any_list) // num
    result = []
    
    if not section:
        return f'The list is empty or less than num'
    
    else:
        sub_list = []
        counter = 0
        
        for i in any_list:
            sub_list.append(i)
            counter += 1
            if counter == section:
                result.append(sub_list.copy())
                sub_list.clear()
                counter = 0
        
        if sub_list:
            result.append(sub_list)
        
        return result

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# divide_by = 3
# print(divider(my_list, divide_by))

#6
def string_to_list(strng:str) -> list:
    return [name.strip() for name in strng.split(',')]

# names = 'Dan, Austin, Victor, Piere,Daemon,Eugene'
# print(string_to_list(names))

#7
strng1, strng2, strng3 = 'Hello', 'from', 'Here'
mixed_string = ','.join([strng1, strng2, strng3])

#8
def to_find(data_list:list) -> None: 
    for _, i in zip(range(101), data_list):
        if i == 777:
            return f'Success!'
    else:
        raise ValueError('No such value in range 100')

# data_list = [random.randrange(0, 1000) for _ in range(200)]
# data_list2 = ['a' * 200]
# print(to_find(data_list))
# print(to_find(data_list2))

#9
def filtering(list_to_filter:list, filter_values: list) -> list:
    result = []
    for item in list_to_filter:
        if not item in filter_values:
            result.append(item)
    return result

# list1 = [random.randrange(0, 1000) for _ in range(100)]
# list2 = [random.randrange(0, 1000) for _ in range(100)]
# start = time.time()
# print(filtering(list1, list2))
# end = time.time()
# print(f'{(end-start) * 1000} ms')