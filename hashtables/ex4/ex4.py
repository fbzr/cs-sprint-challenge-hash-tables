def has_negatives(numbers):
    result = []
    data = {}

    # which positive numbers have corresponding negative numbers in the list.
    # loop through numbers
    for number in numbers:
        # check if the oposite (+ or -) correnponding number is in hash table
        if number * -1 in data:
            # add positive number to result list
            if number < 0:
                result.append(number * -1)
            elif number > 0:
                result.append(number)
        
        # add number in hash table
        data[number] = number

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
