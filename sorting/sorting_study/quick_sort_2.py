import random
from random import randint

def partition(l,h):
    pivot = array[l]
    print("pivot : " + str(pivot))
    # pivot = random.choice(array)
    i = l
    j = h 


    while i<j:

        #terminition conditions
        while (i <= h and array[i] <= pivot):
            i+=1

        while (array[j] > pivot):
            j-=1

        if i<j:
            array[i], array[j] = array[j], array[i]

        print("sorted before " +str(array))


    array[l], array[j] = array[j], array[l]

    print("sorted " +str(array))



    return j


def quick_sort(l,h):
    if array is None:
        return
    if len(array) <= 1:
        return

    if l<h:

        rand_index = (l+h)//2
        # rand_index = randint(l,h)
        print ("rand_index  :  " + str(rand_index))
        array[l], array[rand_index] = array[rand_index], array[l]
        print(" - l : " + str(l) + " - h :" + str(h))
        j = partition(l, h)
        quick_sort(l,j-1)
        quick_sort(j+1,h-1)


# array = [10,16,8,12,15,6,3,9,5]
array = [1,1,1,1,1,1,1]
# array = [10,7,8,2,15,14]


quick_sort(0, len(array) - 1) 
print(array)