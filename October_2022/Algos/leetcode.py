def count_Operation(int1, int2):
    count = 0
    while int1 != 0 and int2 != 0:
        if int1 > int2:
            int1 -= int2
            count += 1
        else:
            int2 -= int1
            count += 1
        return count
    
count_Operation(100, 50)