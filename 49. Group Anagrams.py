class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # hash table to record types of anagrams
        t = {}
        n = len(strs)
        
        # go over each str in strs
        for i in range(n):
            str_ = strs[i]
            # sort the letters in str
            str_ = "".join(sorted(str_))
            
            # group the anagrams together in hash table
            if str_ in t:
                t[str_].append(i)
            else:
                t[str_] = [i]
            
        res = []
        
        # group the anagrams together in hash table into res
        for key in t:
            group = [strs[x] for x in t[key]]
            res.append(group)
            
        return res
            
            