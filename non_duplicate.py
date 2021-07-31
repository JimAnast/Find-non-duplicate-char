def findNonDuplicate(A):
    # Given an input list A of character, which is sorted in an increasing order,
    # and each character is duplicated except one which corresponds to the non-duplicate character in the list.
    # you need to find the non duplicate character
    # Your code below

    uniqueElement=''

    low = 0
    high = len(A) - 1
    def spot_non_duplicate(given_list, low, high):
        if low > high:
            return None
        if low == high:
            return given_list[low]

        mid = int(low + (high - low) / 2)

        if mid % 2 == 0:                                                 #We can observe that if mid is even and its value
            if given_list[mid] == given_list[mid + 1]:                   #is equal to its next element mid+1, then the non duplicate
                return spot_non_duplicate(given_list, mid + 2, high)     #element that we are looking for is on the right half,
            else:                                                        #else it's on the left half
                return spot_non_duplicate(given_list, low, mid)

        else:                                                            #If mid is odd, it's the opposite case from before.
            if given_list[mid] == given_list[mid - 1]:
                return spot_non_duplicate(given_list, mid + 1, high)
            else:                                                        #If mid is an odd number, it cannot be the
                return spot_non_duplicate(given_list, low, mid - 1)      #non duplicate element.
    uniqueElement = spot_non_duplicate(A, low, high)
    return uniqueElement

if __name__ == "__main__":
    assert findNonDuplicate(['c','c','d','d','f','f','z']) == 'z'
    assert findNonDuplicate(['a','a','b','b','c','d','d','e','e','r','r']) == 'c'
    F = ['c','c','d','d','g','g','i','i','k','y','y','z','z']
    dublic_char = findNonDuplicate(F)
    print("The non dublicate character is:", dublic_char)
    G = [1, 1, 3, 3, 6, 6, 7, 7, 8, 9, 9]                            #It can work for inputs of both numbers and letters
    dublic_char = findNonDuplicate(G)                                #of the alphabet. We give examples of both cases
    print("The non duplicate character is:", dublic_char)            #and we print the results.
