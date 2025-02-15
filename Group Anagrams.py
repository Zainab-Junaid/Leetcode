class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for elem in strs:
            s = ''.join(sorted(elem))
            if s in anagram:
                anagram[s].append(elem)
            else:
                anagram[s] = [elem]
        return list(anagram.values())
        
