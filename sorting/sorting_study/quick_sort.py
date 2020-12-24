import random
from random import randint

def partition(array, start, end):
    print("First start index : " + str(start) + "  -  First end index: " + str(end))

    pivot = array[start]
    low = start + 1
    high = end

    print("First pivot index : " + str(pivot) + " - low : " + str(array[low]) + " - high : " + str(array[high]))

    while True:
        print("Inside While array : " + str(array))
        print("Inside start end array : " + str(array[start:end+1]))
        print("Inside While pivot : " + str(pivot) + " - low : " + str(array[low]) + " - high : " + str(array[high]))
        print("Inside While index low : " + str(low) + " - high : " + str(high))

        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1
            try:
                print("Change high : " + " - low : " + str(array[low]) + " - high : " + str(array[high]))
                print("Change high  index: " + " - low : " + str(low) + " - high : " + str(high))
            except Exception as e:
                print("ERR : " + str(e))

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1
            try:
                print("Change low : " + " - low : " + str(array[low]) + " - high : " + str(array[high]))
                print("Change low index : " + " - low : " + str(low) + " - high : " + str(high))

            except Exception as e:
                print("ERR : " + str(e))

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            print(" =========== Swap : " + " - low : " + str(array[low]) + " - high : " + str(array[high]))
            print(" =========== Swap index : " + " - low : " + str(low) + " - high : " + str(high))
            # The loop continues
        else:
            # We exit out of the loop
            print(" ====================== break ======================")
            break

    print(" =========== Before big swap arr : "  + str(array))
    array[start], array[high] = array[high], array[start]
    print(" =========== Swap big : " + " - low : " + str(low) + " - high : " + str(high) + " -  start  : " + str(start))
    print(" =========== After big swap arr : "  + str(array))
    print(" ========================  Going next case =====================")

    return high

def partition_2(nums, left, right):
    # 1. select pivot element and move to first
    pivot_index = (left+right)//2
    pivot = nums[pivot_index]
    # move pivot to end
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

    # 2. move all smaller element to the left
    store_idx = left
    for i in range(left,right):
        if nums[i]<pivot:
            nums[store_idx], nums[i] = nums[i], nums[store_idx]
            store_idx = store_idx + 1

    # 3 . move pilot to the final place , partition position 
    nums[right], nums[store_idx] = nums[store_idx], nums[right]
    return store_idx


def quick_sort(array, start, end):

    if start >= end:
        print(":: start >= end.  >>>>> " + str(start) + " >=  " +  str(end))
        return

    p = partition_2(array, start, end)
    print("Partition index : " + str(p))
    print("Partition : " + str(array[p]))

    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


array = [10,11,8,3]
array = [10, 7, 8, 2, 3, 6]
# array = [1,1,1,1,1,1]


quick_sort(array, 0, len(array) - 1)

print(array)


# A  = [10, 7, 8, 2, 3, 6]

# pivot : 7  >  [7, 10, 8, 2, 3, 6] > A = [2, 6, 3, 7, 8, 10]

# pivot : 2  > [2, 6, 3] 

# pivot : 6 > [6, 3] > A = [2, 3, 6, 7, 8, 10]

# pivot : 8  > [8, 10]  >  X 

# result =  [2, 3, 6, 7, 8, 10]




# pivot = 15 - [15, 7, 8, 2, 10, 14]  
# Array = [14, 7, 8, 2, 10, 15]

# pivot : 7 - [7, 14, 8, 2, 10]  
# Array = [2, 7, 8, 14, 10, 15]



# pivot : 14 - [2, 7, 14, 8, 10, 15] >>  [14, 8, 10] 
# Array : [2, 7, 10, 8, 14, 15]

# pivot : 8 - [8, 10]


# pivot : 14  - [14, 10] >>> 















