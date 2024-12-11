def find_min_max(arr):
    smallest = min(arr)
    largest = max(arr)
    return smallest,largest
arr=[3,5,7,2,8]
smallest,largest = find_min_max(arr)
print(f"smallest:{smallest},largest:{largest}")
