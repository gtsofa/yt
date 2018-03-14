# Searching an item in a list - using sequential search technique

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True

        else:
            pos = pos + 1

    return found

print(sequentialSearch([3,7,9,11,17], 8))
print(sequentialSearch([15, 18, 2, 19, 18, 0, 8, 14, 19, 14], 18))