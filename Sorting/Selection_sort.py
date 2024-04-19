class Selection_Sort:
    def selection_sort(self, arr):
        n=len(arr)
        for i in range(n-1):
            min_index=i
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[i], arr[min_index]= arr[min_index], arr[i]
        return arr

#Example case

    arr=[64, 25, 12, 22, 11]
    selection_sort(arr)
    print("The sorted array is ",arr)