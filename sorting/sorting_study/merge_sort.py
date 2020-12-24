def merge(left, right, arr):
    print("first visit merge- first arr : " + str(arr) + " -  Size List : " + str(len(arr)))
    print("first visit merge- first right : " + str(right))
    print("first visit merge- first left : " + str(left))
    # Two iterators for traversing the two halves
    i = 0
    j = 0

    # Iterator for the main list
    k = 0

    while i < len(left) and j < len(right):
        print("before 111 sort  i , j , k : " +  str(i) + str(j) + str(k))
        if left[i] < right[j]:
            # The value from the left half has been used
            arr[k] = left[i]
            print(" >>>>> matching i arr["+str(k)+"] = left["+ str(i) +"] " +  str(arr[k]) + " = " + str(left[i]) )

            # Move the iterator forward
            i += 1
        else:
            arr[k] = right[j]
            print(" >>>>> matching j arr["+str(k)+"] = left["+ str(j) +"] " +  str(arr[k]) + " = " + str(right[j]) )

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
        print("after 2 sort - first arr : " + str(arr) + " -  Size List : " + str(len(arr)))

    while j < len(right):
        arr[k]=right[j]
        j += 1
        k += 1
        print("after 3 sort - first arr : " + str(arr) + " -  Size List : " + str(len(arr)))



def sort(arr, t):
    print(" >>>>>>> first arr : " + str(arr) + " -  Size List : " + str(len(arr)) +  " -  Type : " + t)
    if len(arr) > 1:
        mid = len(arr) // 2
        print("mid : " + str(mid) + " Val : " + str(arr[mid]))
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        sort(left, "l")
        sort(right, "r")
        merge(left, right, arr)
        print("===================")
 


arr = [54,26,93,17,77]
sort(arr, "")
print(arr)
