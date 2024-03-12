# For fib1(5) the number of calls were around 15 as its a tree recursion. 
# Fibonacci numbers computation is recursive in nature and its structure is represented by a recursion tree
# nth fibonacci number is used as the root of the tree. 
# The left subtree represents the computation of the n-1st Fibonacci number
# The right subtree represents the computation of the n-2nd Fibonacci number 

# Fibonacci series using recursion
number_recursive_calls = 0


def fib1(n: int) -> int:
    global number_recursive_calls
    number_recursive_calls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2) 
    raise NotImplementedError()


if __name__ == "__main__":
    print(fib1(15))
    print(number_recursive_calls)


loop_iterator = 0

# Fibonacci using iteration


def fib2(n: int) -> int:
    a, b = 1, 1
    global loop_iterator
    loop_iterator += 1
    for i in range(n):
        a, b = b, a + b
    return a
    raise NotImplementedError()


if __name__ == "__main__":
    print(fib2(15))
    print(loop_iterator)


if __name__ == "__main__":
    print(fib1(23))
    print("Number of function calls for fib1: ", number_recursive_calls)
    print(fib2(23))
    print("Number of loop iterations for fib2: ", loop_iterator)