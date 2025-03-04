def bubble_sort(arr):
    length = len(arr)
    swapped = True
    for count in range(length -1):
        if not swapped:
            break
        swapped = False
        for counter in range(length - count -1):
            if arr[counter] > arr[counter+1]:
                arr[counter], arr[counter+1] = arr[counter+1], arr[counter]
                swapped = True



arr = [50,2,4,1,6,8,0,7,50]
bubble_sort(arr)
print(arr)