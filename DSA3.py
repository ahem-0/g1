def permute(arr, l, r, result):
    if l == r:
        result.append(arr[:])
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l + 1, r, result)
            arr[l], arr[i] = arr[i], arr[l] 

arr = [1, 2, 3]
result = []
permute(arr, 0, len(arr) - 1, result)
print (result)
