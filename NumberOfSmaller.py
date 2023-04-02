def findSmaller(nums1:list[int], nums2:list[int]) -> list[int]:
    smallerElements = []
    ptr = 0

    for i in nums2:
        count = 0 if not smallerElements else smallerElements[-1]
        while ptr < len(nums1) and nums1[ptr] < i:
            count += 1
            ptr += 1
        smallerElements.append(count)
    return smallerElements


length1, length2 = list(map(int, input().split()))
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

smallerElements = findSmaller(nums1, nums2)
print(*smallerElements)
