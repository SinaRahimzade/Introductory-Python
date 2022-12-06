
from termcolor import colored

def color_index(array, index, color):
    for i in range(len(array)): 
        if i == index:
            print(colored(array[i], color), end=', ')
        else:
            print(array[i], end=', ')

array = [5, 2, 4, 6, 1, 3]
# visualize the sorting algorithms
def selection_sort(array):
    for i in range(len(array)):
        # print sorted part of the array in green
        print(colored(array[:i], 'green'), end='')
        # print unsorted part of the array in red
        print(colored(array[i:], 'red'))
        # find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # swap the minimum element with the first element of the unsorted part
        array[i], array[min_index] = array[min_index], array[i]
        # print the swapped array in blue
        print(colored(array, 'blue')) 
    return array


def insertion_sort(array):
    for i in range(1, len(array)):
        # print sorted part of the array in green
        print(colored(array[:i], 'green'), end='')
        # print unsorted part of the array in red
        print(colored(array[i:], 'red'))
        # insert the first element of the unsorted part into the sorted part
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        # print the swapped array in blue
        print(colored(array, 'blue')) 
    return array




insertion_sort(array)