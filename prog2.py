def partition(arr, value):
    smaller = []
    larger = []

    for num in arr:
        if num < value:
            smaller.append(num)
        else:
            larger.append(num)

    return [smaller, larger]



input_array = [1, 4, 2, 5, 3, 7]
split_value = 3
result = partition(input_array, split_value)

