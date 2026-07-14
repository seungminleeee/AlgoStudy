class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)

        mxarea = 0
        for i in range(N):
            for j in range(i+1, N):
                area = min(heights[i],heights[j]) * (j-i)
                if area > mxarea:
                    mxarea = area
        
        return mxarea