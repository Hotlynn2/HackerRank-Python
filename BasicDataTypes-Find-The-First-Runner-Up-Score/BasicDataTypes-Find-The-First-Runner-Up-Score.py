# seed random number generator
seed(1)

n = int(input())

# generate some integers
for _ in range(n):
	value = randint(-100, 100)
	print(value)