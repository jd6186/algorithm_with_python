import time
inputDatas = [1, 10, 34, 4, 9, 6, 7, 8, 5, 2]

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)
print(time.time())
quick_sort(inputDatas)

#inputDatas.sort()
# 시간 값을 비교하면 sort()도 퀵정렬로 되는 것을 알 수 있다.
print(time.time())
print(inputDatas)