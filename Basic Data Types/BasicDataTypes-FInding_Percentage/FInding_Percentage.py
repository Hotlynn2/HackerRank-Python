if __name__ == '__main__':
    n = int(input())
    student_name = []
    student_score = []
    
    for _ in range(n):
        score_data = str(input()).split()
        
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()