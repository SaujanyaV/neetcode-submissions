class Solution:
    def maxArea(self, heights: List[int]) -> int:
        st = 0
        en = len(heights) - 1
        max_area = 0

        while st < en:
            max_area = max(max_area, self.getArea(st, en, heights))

            if heights[st] > heights[en]:
                en -= 1
            else:
                st += 1
        
        return max_area


    def getArea(self, st, en, heights):
        return (en - st) * min(heights[st], heights[en])