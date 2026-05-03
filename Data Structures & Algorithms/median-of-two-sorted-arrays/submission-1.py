class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 # Target size for the left partition
        
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)
        while l <= r:
            i = (l + r) // 2  # i = number of elements from A
            j = half - i      # j = number of elements from B

            # If i is 0, nothing on the left. If i is len(A), nothing on the right.
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    # Odd: The median is the smallest value in the right half
                    return min(Aright, Bright)
                # Even: Average of max-left and min-right
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                # Too many elements from A, move the pointer left
                r = i - 1
            else:
                # Too many elements from B, move the pointer right
                l = i + 1
                