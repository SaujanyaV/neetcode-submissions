class Solution:
    def trap(self, height: List[int]) -> int:
        
        st, en = 0, len(height) - 1
        ans = 0
        max_left, max_right = 0, 0

        while st < en:
            if height[st + 1] < height[st]:
                break
            st += 1
        
        while st < en:
            if height[en - 1] < height[en]:
                break
            en -= 1
        
        while st < en:
            max_left, max_right = max(max_left, height[st]), max(max_right, height[en])

            if max_right >= max_left:
                if height[st+1] < max_left:
                    ans += max_left - height[st+1]
                    st += 1
                else:
                    st += 1
            
            if max_left > max_right:
                if height[en-1] < max_right:
                    ans += max_right - height[en-1]
                    en -= 1
                else:
                    en -= 1
            
        
        return ans
            