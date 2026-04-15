class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        product = 1
        result = []

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

            if zero_count > 1:
                return [0] * len(nums)
        
        for num in nums:
            if zero_count == 1:
                if num != 0:
                    result.append(0)
                else:
                    result.append(product)
            else:
                result.append(int(product / num))
                
        return result


