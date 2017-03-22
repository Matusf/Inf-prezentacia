def binary_search(seq, item):
    end    = len(seq) - 1
    start  = 0

    while True:
        middle = (start + end) / 2

        if seq[middle] == item:
            return middle
        elif start > end:
            return -1
        elif item > seq[middle]:
            start = middle + 1
        elif item < seq[middle]:
            end = middle - 1

with open('binary_search.txt', 'r') as f:
    a = f.readline()
    for line in f:
    print(binary_search(seq, int(line.strip())))
