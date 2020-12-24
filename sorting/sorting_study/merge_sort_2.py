def mergeSort(arr, t):
    print(" >>>>>>> first arr : " + str(arr) + " -  Size List : " + str(len(arr)) +  " -  Type : " + t)

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        mergeSort(left, "l")
        mergeSort(right, "r")
        print("==================== ")

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        print("first visit merge- first arr : " + str(arr))
        print("first visit merge- first left : " + str(left))
        print("first visit merge- first right : " + str(right))

        while i < len(left) and j < len(right):
            print("look left[i] < right[j]: " +  str(left[i]) + " < " +  str(right[j]))
            if left[i] < right[j]:

              # The value from the left half has been used
              arr[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                arr[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
            # print("after 111 sort  i , j , k : " +  str(i) + str(j) + str(k))
            print("after 111 sort - first arr : " + str(arr) + " -  Size List : " + str(len(arr)))

        print("after 1 sort - first arr : " + str(arr) + " -  Size List : " + str(len(arr)))
        print("after 1 sort  i , j , k : " +  str(i) + str(j) + str(k))

        # For all the remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            print("333 sort - first arr : " + str(arr) + " -  Size List : " + str(len(arr)))


        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1
            print("444 sort - first arr : " + str(arr) + " -  Size List : " + str(len(arr)))


arr = [54,26,93,17,77]
mergeSort(arr, "")
print(arr)
