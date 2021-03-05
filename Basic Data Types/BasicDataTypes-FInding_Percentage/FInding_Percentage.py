if __name__ == '__main__':
    import statistics 

    n = int(input())
    student_name = []
    student_score = []
    
    
    for _ in range(n):
        score_data = str(input()).split()
        student_name.append(score_data[0])
        student_score.append(int(score_data[1:]))

    query_name = input()
    
    '''score_int = []
    for score in student_score:
        score_int.appendint()'''

    students = dict(zip(student_name, student_score))  
    print(students)     

    #student_names = student_name.split()
    for name,score in students.items():
            if (name == query_name): 
                average = sum(score) / 3
    print(average)           

        

    print(student_name)
    print(student_score[0])



