def numbers(limits):
    i = 0
    numbers = []

    while i < limits:
        numbers.append(i)
        i += 1
    return numbers


user_limit = int(input("Give a limit: "))
print(numbers(user_limit))