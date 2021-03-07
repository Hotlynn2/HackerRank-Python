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
    
    students = dict(zip(student_name, student_score))     

    #student_names = student_name.split()
    for name,score in students.items():
            if (name == query_name): 
                score_int = []
                for actual_scores in score:
                    score_int.append(int(actual_scores))
                    average = sum(score_int) / 3
                    average = "{:.2f}".format(average)
    
    print(average)           

    



