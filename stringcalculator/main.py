import re

def add(numbers):
    """Add numbers from a given string

    Args:
        string (str): String containing numbers and delimeter

    Raises:
        ValueError exception:  When negative numbers are incountered

    Returns:
        Integer (int): Summation of the given numbers 
    """

    if numbers=="":
        return 0

    count=0
    for i in range(len(numbers)):
        if numbers[i].isdigit()==False:
            count+=1
    if count==0:
        return int(numbers)

    numbers = list(map(int, re.findall(r"-?\d+", numbers)))
    if any(num < 0 for num in numbers):
        raise ValueError("Negatives are not allowed " + str([num for num in numbers if num < 0]))

    numbers = list(filter(lambda x : x<1000, numbers))
    return sum(numbers)


if __name__ == '__main__':
    print(add(input()))