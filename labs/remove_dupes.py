"""
- Given an array of N element which contains elements from ) to N-1, with any of
these numbers appearing any number of times.
- Find these repeating numbers in O(N) and using only constant memory space.
- for example, let N be 7 and array be [1, 2, 3, 1, 3, 6, 6].
  The answer is 1, 3, and 6

  traverse the list from 0 to N-1 {
    check for sign of A[abs(A[i)]
    if positive then
        make it negative by A[abs(A[i])] = - A[abs(A[i])]
    else // i.e., A[abs[A[i])] is negative
        this element (ith element of list) is a repetition
    }

    Note: The program doesn't handle 0 case(if 0 is present in array).
    The program can be easily modifeld to handle that also. It is not
    handled to keep the code simple.
    Time complexity: O(N)
    Auxiliary Space: O(1)
"""


def remove_duplicates(arr):

    a = []  # array to store non-duplicate numbers
    print("The repeating elements are: \n")

    for i in range(0, len(arr)):
        if(arr[abs(arr[i])]) >= 0:
            a.append(arr[abs(arr[i])])
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:  # i.e., A[abs(A[i])] is negative
            print(abs(arr[i]))

    print(a)
    return len(a)


def main():
    A = [1, 2, 3, 1, 3, 6, 6]
    print(remove_duplicates(A))

main()
