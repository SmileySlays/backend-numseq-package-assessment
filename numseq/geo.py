def square(n):
    """Returns nth  number squared"""
    return(n * n)


def triangle(n):
    """Returns the nth triangle number"""
    count = 0
    for num in range(1, n+1):
        count += num
    return(count)


def cube(n):
    """Returns nth number cubed"""
    return(n * n * n)


if __name__ == "__main__":
    import sys
    cube(int(sys.argv[1]))