def fib(n):
    """Returns nth fibonacci number"""
    fib_list = []
    for num in range(n+1):
        if num == 0 or num == 1:
            fib_list.append(num)
        else:
            fib_list.append(fib_list[-2] + fib_list[-1])
    return(fib_list[-1])


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))