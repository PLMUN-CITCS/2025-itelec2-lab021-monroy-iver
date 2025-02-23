# Iver John Monroy
# ITELEC2
# Laboratory # 21 - Group Activity # 01 - Problem 03: Factorial Calculator with Input and Calculation Functions


def get_non_negative_integer():
    num = int(input("Enter a non-negative integer: "))
    return num

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

def main():
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()