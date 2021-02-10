marksheet = []
scoresheet = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        marksheet = marksheet + [[name, score]]
        score = score + [score] 