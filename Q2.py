# Question No. 2: Write Python code to find the factorial of 5 using a Recursive Function.
def fact(num, factorial):
    if num == 0 or num == 1:
        return 1
    else:
        num = num - 1
        factorial = factorial * num
        if num > 1:
            return fact(num, factorial)
        else:
            return factorial
num = 5
print(f"Factorial is: ", fact(num, factorial=num))
