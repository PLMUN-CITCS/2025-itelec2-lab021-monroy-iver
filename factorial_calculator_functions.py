# Iver John Monroy
# ITELEC2
# Laboratory # 21 - Group Activity # 01 - Problem 03: Factorial Calculator with Input and Calculation Functions


def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Please enter a valid non-negative integer.")
            return
        
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        
        print(f"The factorial of {num} is: {factorial}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()