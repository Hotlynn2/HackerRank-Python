if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    highest_number = max(arr)
    
    
    highest_number_count = arr.count(highest_number)
    

    for i in range(highest_number_count):
        arr.remove(highest_number)
    print(max(arr))