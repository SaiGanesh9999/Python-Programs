class NumArray:

    def __init__(self, nums: list[int]):
        n=len(nums)
        self.pf=[0]*(n+1)
        self.pf[0]=nums[0]
        for i in range(1,n):
            self.pf[i]=self.pf[i-1]+nums[i]
    def sumRange(self, left: int, right: int) -> int:
        return self.pf[right]-self.pf[left-1]
