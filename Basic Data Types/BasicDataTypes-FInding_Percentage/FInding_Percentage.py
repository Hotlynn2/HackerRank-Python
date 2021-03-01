if __name__ == '__main__':
    import statistics 

    n = int(input())
    student_name = []
    student_score = []
    
    
    for _ in range(n):
        score_data = str(input()).split()
        student_name.append(score_data[0])
        student_score.append(score_data[1:])

    query_name = input()

    student_names = student_name.split()
    for name in student_names:
        if (name == query_name) and (name.index() == student_score.index()):
            sum(student_score[name.index()]) / 3
            

    print(student_name)
    print(student_score)




    
    if (query_name in student_name) and (student_score.index == student_name.index):
        average = student_score.mean()
    print(average)
    
    if (query_name in student_name) and (student_score.index == student_name.index):
        average = student_score.mean()
    print(average)
    if (query_name in student_name) and (student_score.index == student_name.index):
        average = student_score.mean()
    print(average)
    
    
    

        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()