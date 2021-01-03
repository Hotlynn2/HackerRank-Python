if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    from random import seed
    from random import randint

    # seed random number generator
    seed(1)

    n = int(input())

    # generate some integers
    for _ in range(n):
        value = randint(-100, 100)
	num = range(20,58)
	print(value)