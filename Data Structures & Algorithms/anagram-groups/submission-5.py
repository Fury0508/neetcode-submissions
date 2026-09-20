class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs: 
            sig = "".join(i for i in  sorted(word))
            group[sig].append(word)
        return list(group.values())