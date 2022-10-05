def solution(number):
    ammount = [num for num in range(number) if num % 3 == 0 or num % 5 == 0]
    return sum(ammount)

print(solution(6))