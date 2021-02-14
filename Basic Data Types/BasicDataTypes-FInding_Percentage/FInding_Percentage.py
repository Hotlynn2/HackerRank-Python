if __name__ == '__main__':
    n = int(input())
    student_name = []
    student_score = []
    
    for _ in range(n):
        score_data = str(input()).split()
        student_name.append(score_data[0])
        student_score.append(score_data[1:])
    print(student_name)
    print(student_score) 
        
        #name, *line = input().split()
        #scores = list(map(float, line))
        #student_marks[name] = scores

    #query_name = input()