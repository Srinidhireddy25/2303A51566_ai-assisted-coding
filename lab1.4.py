#task-01
# #write a program to check whether the given number is prime or not without using functions
#take input from user
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#task-02
#generate optimized version of above code using function
#take input from user
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#generate fibonocci series using iterative function in a given range

def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
num_terms = int(input("Enter the number of terms in Fibonacci series: "))
fib_series = fibonacci_iterative(num_terms)
print("Fibonacci series:")
for num in fib_series:
    print(num)


#generate fibonocci series using recursive function in a given range

def fibonacci_recursive(n, a=0, b=1, fib_series=None):
    if fib_series is None:
        fib_series = []
    if n > 0:
        fib_series.append(a)
        return fibonacci_recursive(n - 1, b, a + b, fib_series)
    return fib_series
num_terms = int(input("Enter the number of terms in Fibonacci series: "))
fib_series = fibonacci_recursive(num_terms)
print("Fibonacci series:")
for num in fib_series:
    print(num)
