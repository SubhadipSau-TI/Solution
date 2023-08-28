def partition(arr, value):
    smaller = []
    larger = []

    for num in arr:
        if num < value:
            smaller.append(num)
        else:
            larger.append(num)

    return smaller,larger



arr = [1, 4, 2, 5, 3, 7]
value = 3
print(partition(arr,value))

