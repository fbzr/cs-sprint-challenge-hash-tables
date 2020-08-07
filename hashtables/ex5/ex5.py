# Your code here



def finder(files, queries):
    ht = {}

    # add every path to ht: key = file name
    for path in files:
        splitted  = path.split("/")

        filename = splitted[len(splitted)-1]
        
        # check same filename in different paths
        if filename in ht:
            ht[filename] += [path]
        else:
            ht[filename] = [path]

    result = []

    for filename in queries:
        if filename in ht:
            result += ht[filename]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
