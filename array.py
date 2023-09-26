import array as arr


# printing an array
def print_1d_array():
    a = arr.array('i', [1, 2, 3, 4, 5])
    b = arr.array('d', [1.5, 2.5, 3.5, 4.5, 5.5])
    print("One Dimensional Integer Array: ", end=" ")
    for i in range(0, len(a)):
        print(a[i], end=" ")
    print("\nOne Dimensional Double Array: ", end=" ")
    for i in range(0, len(b)):
        print(b[i], end=" ")


# accessing elements from an array
def accessing_element_1d_array():
    a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # access 5th element
    print("Array's 5th Element: ", end=" ")
    print(a[4], end=" ")
    # access 10th element
    print("\nArray's 10th Element: ", end=" ")
    print(a[9], end=" ")


# inserting elements into an array
def insert_into_1d_array():
    a = arr.array('i', [10, 20, 30])
    print("Array Before: ", end=" ")
    for i in range(0, len(a)):
        print(a[i], end=" ")
    a.append(40)
    print("\nArray After: ", end=" ")
    for i in range(0, len(a)):
        print(a[i], end=" ")


# updating an element in an array
def update_1d_array():
    a = arr.array('i', [10, 20, 30])
    print("Array Before: ", end=" ")
    for i in range(0, len(a)):
        print(a[i], end=" ")
    a[2] = 40
    print("\nArray After: ", end=" ")
    for i in range(0, len(a)):
        print(a[i], end=" ")


# removing elements from an array
def removing_elements_1d_array():
    a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Existing Array: ", end=" ")
    for i in range(0, len(a)):
        print(a[i], end=" ")
    # remove 5th element
    a.pop(4)
    print("\nAfter removing 5th Element: ", end=" ")
    for i in range(0, len(a)):
        print(a[i], end=" ")
    # remove 9th element
    a.pop(8)
    print("\nAfter removing 9th Element: ", end=" ")
    for i in range(0, len(a)):
        print(a[i], end=" ")


# Slicing: To print a specific range of elements from an array slicing method is used.
# to print elements from beginning to a range use: [:Index]
# to print elements from end use: [:-Index]
# to print elements from specific index till the end use: [Index:]
# to print elements within a range use: [Start Index:End Index]
# to print the entire array with the use of slicing operation use: [:]
# to print the entire array in reverse order use: [::-1]
def slicing_1d_array():
    a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Initial Array: ")
    for i in range(0, len(a)):
        print(a[i], end=" ")
    # using slice operation
    sliced_array = a[:5]
    print("\nSlicing elements from beginning till 5th: ", end=" ")
    print(sliced_array)
    sliced_array = a[:-2]
    print("\nSlicing elements from end till 8th element: ", end=" ")
    print(sliced_array)
    sliced_array = a[8:]
    print("\nSlicing elements from index till end: ", end=" ")
    print(sliced_array)
    sliced_array = a[3:6]
    print("\nSlicing elements in a range 3-6: ", end=" ")
    print(sliced_array)
    sliced_array = a[:]
    print("\nFull array with slicing: ", end=" ")
    print(sliced_array)
    sliced_array = a[::-1]
    print("\nFull array reverse order: ", end=" ")
    print(sliced_array)


# searching element in an array
def search_1d_array():
    a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Initial Array: ")
    for i in range(0, len(a)):
        print(a[i], end=" ")
    # search element at index
    print("\nValue at 5th index is: ", end=" ")
    print(a.index(5))


# FUNCTIONS
# counting elements in an array
def count_occurrence_1d_array():
    a = arr.array('i', [1, 2, 3, 4, 5, 5, 5, 9, 8, 7, 6])
    count = a.count(5)
    print("No. of occurrences of 5: ", count)


# reverse an array
def reverse_1d_array():
    a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    a.reverse()
    print("Reversed Array: ", *a)


# extend elements for an array
def extend_1d_array():
    a = arr.array('i', [1, 2, 3, 4, 5])
    a.extend([6, 7, 8, 9, 10])
    print("Extended Array: ", *a)


if __name__ == "__main__":
    # printing an existing array
    print_1d_array()
    # accessing an element
    accessing_element_1d_array()
    # insert
    insert_into_1d_array()
    # update
    update_1d_array()
    # removing elements
    removing_elements_1d_array()
    # slicing
    slicing_1d_array()
    # searching
    search_1d_array()
    # count the occurrence of an element in an array
    count_occurrence_1d_array()
    # reverse an array
    reverse_1d_array()
    # extend an array
    extend_1d_array()
