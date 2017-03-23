def fib(n):
    if n <= 2:                  # 1. a 2. člen je 1
    return 1
    return fib(n-1) + fib(n-2)  # N-tý člen je súčet dvoch predošlých

with open(fibonacci.txt, r) as f:
    for line in f:
        print(fib(line.strip))
