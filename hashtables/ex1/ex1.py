def get_indices_of_item_weights(weights, length, limit):
    # return indices of two items that sum 21
    # limit is the constant
    # I need to look for item by its weight and access its index
    # need to loop through list and add each weight to dict. Format [weight]: index
    # The higher valued index should be placed in the zeroth index and the smaller
    ht = {}

    for (index, weight) in enumerate(weights):
        if weight <= limit:
            # find the necessary weight to pair/sum with current that result limit
            rest = limit - weight
            # check if that number has been added to the ht as key and access its index (value in the ht)
            if rest in ht:
                return (index, ht[rest])

        # if it didn't find the pair, add value to ht
        ht[weight] = index

    return None