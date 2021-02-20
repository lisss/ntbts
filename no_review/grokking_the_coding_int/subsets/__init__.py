def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        # we will take all existing subsets and insert the current number
        # in them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and insert the current element to it
            set1 = list(subsets[i])
            set1.append(currentNumber)
            subsets.append(set1)

    return subsets


def find_subsets_with_duplicates(nums):
    subsets = []
    nums = sorted(nums)
    subsets.append([])

    for i in range(len(nums)):
        num = nums[i]
        n = len(subsets)
        start = 0
        if i and nums[i - 1] == num:
            start = i
        for j in range(start, n):
            set1 = list(subsets[j])
            set1.append(num)
            subsets.append(set1)
    return subsets


# print(find_subsets([1, 3, 3]))
print(find_subsets_with_duplicates([1, 5, 3, 3]))
