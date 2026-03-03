#bài 6
def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
                swapped = True
        if not swapped:
            break
    return arr, swap_count

my_list = [64, 34, 25, 12, 22, 11, 90]

sorted_list, swaps = bubble_sort(my_list)

print("Danh sách đã sắp xếp là:", sorted_list)
print("Số lần hoán đổi được thực hiện:", swaps)
