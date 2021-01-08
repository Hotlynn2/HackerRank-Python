if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    highest_number = max(arr)
    print(highest_number)
    
    highest_number_count = arr.count(highest_number)
    print(highest_number_count)

    for i in highest_number_count:
        arr.remove(highest_number)
    print(arr)