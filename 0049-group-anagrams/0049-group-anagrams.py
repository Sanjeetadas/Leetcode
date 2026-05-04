class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        from collections import defaultdict
    
        anagram_map = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)  
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
        