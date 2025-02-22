def is_prime(input_number):
    if input_number < 2:
        return False
    for i in range(input_number - 1, 1, -1):
        if input_number % i == 0:
            return False
    return True

number = int(input("Enter a number:"))
if is_prime(number):
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")