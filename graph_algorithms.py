# create a recursive function to generate Fibonacci numbers
#step 1
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(20):
    print(f"F({i}) = {fibonacci_recursive(i)}")

#step 2
# create an iterative function to generate Fibonacci numbers

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


for i in range(20):
    print(f"F({i}) = {fibonacci_iterative(i)}")

#step3
#create a function to measure the execution time of both approaches
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")


#step 4
#create a generator function that yields Fibonacci numbers:
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

#step5
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")



#task 1
def fibonacci_up_to_n(n):
    fib_sequence = [0, 1]
    
    
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:
            break
        fib_sequence.append(next_fib)
    
    return fib_sequence
n = 100
print("Fibonacci sequence up to", n, ":", fibonacci_up_to_n(n))



#task 2 
def fibonacci(n, memo={}):
    # Base cases
    if n <= 1:
        return n
    # Check if result is already in memo
    if n not in memo:
        # Recursive calculation with memoization
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(fibonacci(40))  



#task 3
import math

def is_fibonacci_number(n):
    # Check if 5 * n^2 + 4 or 5 * n^2 - 4 is a perfect square
    def is_perfect_square(x):
        s = int(math.isqrt(x))
        return s * s == x
    
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

number = 200
if is_fibonacci_number(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is not a Fibonacci number.")



#task 4
def fibonacci_ratios(terms):
    if terms < 2:
        print("Need at least 2 terms to calculate ratios.")
        return

    
    a, b = 0, 1
    ratios = []

    for _ in range(terms - 1):
        # Calculate the ratio of b to a (ignoring the first term 0)
        if a != 0:
            ratio = b / a
            ratios.append(ratio)
            print(f"Ratio of F{_ + 2} / F{_ + 1}: {ratio}")

        # Move to the next Fibonacci numbers
        a, b = b, a + b

    return ratios

# Example usage
terms = 45
ratios = fibonacci_ratios(terms)
print("\nRatios approaching the golden ratio:", ratios)




