def intersection(arrays):
    # loop through first list
        # add every element to dict as key
    dataset = {}
    for item in arrays[0]:
        dataset[item] = 1
    
    result = []
    # go through every list
    # index will represent how many lists we have looped through
    for index, current_list in enumerate(arrays[1:], 1):
        for item in current_list:
            # increment items value in hash table
            if item in dataset:
                dataset[item] += 1
                # if it is the last list: if items value in ht matches with the number of arrays checked, add item to result array
                if index == len(arrays) - 1 and dataset[item] == len(arrays):
                    result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
