class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        # creting bucket=
        #  bucket[i] = numbers appearing i times
        bucket = [[] for _ in range(len(nums)+1)]
        for num,count in freq.items():
            bucket[count].append(num)
        result = []
        for count in range(len(bucket) -1,0,-1):
            for num in bucket[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result