# prime_checker.py

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    number_to_check = 29  # You can change this number to test different inputs
    if is_prime(number_to_check):
        print(f"{number_to_check} is a prime number.")
    else:
        print(f"{number_to_check} is not a prime number.")
