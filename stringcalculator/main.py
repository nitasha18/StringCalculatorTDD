def add(numbers):
    if numbers=="":
        return 0

    count=0
    for i in range(len(numbers)):
        if numbers[i].isdigit()==False:
            count+=1
    if count==0:
        return int(numbers)

    numbers=numbers.split(",")
    numbers=[int(num) for num in numbers]
    return sum(numbers)