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

    man = dict(zip(student_name, student_score))  
    print(man)     

    #student_names = student_name.split()
    for key,value in iterstudent_name:
            if (name == query_name) and (student_name.index(name) == student_score.index(student_name):
                sum(student_score[name.index()]) / 3
        

    print(student_name)
    print(student_score[0])



