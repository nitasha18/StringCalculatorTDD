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

    empty_string = ""
    none_type = None
    digit_count = 0
    numbers_regex = "-?\\d+"
    calculator_limit = 1000

    if numbers == none_type:
        return -1

    if numbers == empty_string:
        return 0

    for i in range(len(numbers)):
        if numbers[i].isdigit()==False:
            digit_count+=1
    if digit_count==0:
        return int(numbers)

    numbers = list(map(int, re.findall(numbers_regex, numbers)))

    if any(number < 0 for number in numbers):
        raise ValueError("Negatives are not allowed " + str([number for number in numbers if number < 0]))

    numbers = list(filter(lambda number : number < calculator_limit, numbers))

    return sum(numbers)


if __name__ == '__main__':
    print(add(input()))