class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}
        for s in strs:
            s_sort = "".join(sorted(s))
            if s_sort not in mapper:
                mapper[s_sort] = [s]
            else:
                mapper[s_sort].append(s)
        return list(mapper.values())
