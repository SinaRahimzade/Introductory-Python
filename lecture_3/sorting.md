# Bubble Sort
Bubble Sort is one of the most straightforward sorting algorithms. Its name comes from the way the algorithm works: With every new pass, the largest element in the list “bubbles up” toward its correct position.
Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent items that are out of order.

![image](https://files.realpython.com/media/python-sorting-algorithms-bubble-sort.216ab9a52018.png)

Bubble sort is a simple algorithm, but it’s not very efficient. It’s not a good choice for sorting large lists. The algorithm’s time complexity is O(n^2), which means that for a list of n elements, the algorithm will have to make n^2 comparisons. The space complexity is O(1), which means that the algorithm only requires a constant amount of space.

## Algorithm
1. Start at the beginning of the list.
2. iterate through the list, comparing each element to its adjacent element.
3. if the element is greater than its adjacent element, swap them.
4. go on to the next element, and repeat steps 2 and 3 until the end of the list.
5. repeat steps 1-4 until the list is sorted.
   
## Implementation
```python
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
```

## Example
```python
>>> bubble_sort([5, 4, 3, 2, 1])
[1, 2, 3, 4, 5]
```

# Selection Sort
Selection sort is another simple sorting algorithm. It works by selecting the smallest element in the list and swapping it with the first element in the list. Then, it selects the second-smallest element in the list and swaps it with the second element in the list. It continues doing this until the list is sorted.

![image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.programiz.com%2Fdsa%2Fselection-sort&psig=AOvVaw0NYd-UTdmcREAXK6yS9FiG&ust=1670503051548000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCJjf8PnC5_sCFQAAAAAdAAAAABAE)

Selection sort is a simple algorithm, but it’s not very efficient. It’s not a good choice for sorting large lists. The algorithm’s time complexity is O(n^2), which means that for a list of n elements, the algorithm will have to make n^2 comparisons. The space complexity is O(1), which means that the algorithm only requires a constant amount of space.

## Algorithm
1. Start at the beginning of the list.
2. find the smallest element in the list.
3. swap the smallest element with the first element in the list.
4. go on to the next element, and repeat steps 2 and 3 until the end of the list.
5. end
   
## Implementation
```python
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
```

## Example
```python
>>> selection_sort([5, 4, 3, 2, 1])
[1, 2, 3, 4, 5]
```

# Insertion Sort
Insertion sort is another simple sorting algorithm. It works by inserting each element into its proper place in the list. It does this by comparing the element to the elements before it and swapping them if necessary.

![image](https://files.realpython.com/media/python-sorting-algorithms-insertion-sort.a102f819b3d7.png)

Insertion sort is a simple algorithm, but it’s not very efficient. It’s not a good choice for sorting large lists. The algorithm’s time complexity is O(n^2), which means that for a list of n elements, the algorithm will have to make n^2 comparisons. The space complexity is O(1), which means that the algorithm only requires a constant amount of space.

## Algorithm
1. Start at the beginning of the list.
2. iterate through the list, comparing each element to its adjacent element.
3. swap the element with its adjacent element if the element is smaller than its adjacent element.
4. go on to the next element, and repeat steps 2 and 3 until the end of the list.
5. end 
   
## Implementation
```python
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array
```

## Example
```python
>>> insertion_sort([5, 4, 3, 2, 1])
[1, 2, 3, 4, 5]
```

