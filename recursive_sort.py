def quicksort(arr):
    if len(arr)<=1:
        return arr
    p=arr[0]
    left=[x for x in arr[1:] if x<=p]
    right=[x for x in arr[1:] if x>p]
    return quicksort(left)+[p]+quicksort(right)
arr=list(map(int,input().split()))
print(quicksort(arr))