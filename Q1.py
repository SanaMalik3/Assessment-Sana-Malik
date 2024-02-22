# Question No. 1: Write Python code to print the first 10 Fibonacci sequences using a Recursive Function.
lst = [0, 1]
def fibonacci_nums(lst):
    if len(lst) < 10:    
        lst.append(lst[-1] + lst[-2])
        fibonacci_nums(lst)
    return lst

print(fibonacci_nums(lst))
