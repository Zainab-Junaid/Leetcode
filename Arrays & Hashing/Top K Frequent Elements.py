class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d_count = {}
        l = []
        for elem in nums:
            if elem in d_count:
                d_count[elem] += 1
            else:
                d_count[elem] = 1
        d = sorted(d_count.items(), key = lambda x: x[1], reverse = True)
        for i in range(k):
            l.append(d[i][0])
            print()
        return l
