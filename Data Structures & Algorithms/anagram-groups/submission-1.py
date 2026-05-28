class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = defaultdict(list)
        # answer = []
        # for words in strs:
        #     sortedWord = ''.join(sorted(words))
        #     groups[sortedWord].append(words)
        
        # for group in groups.values():
        #     answer.append(group)
        # return answer

        hash_s = defaultdict(list)
        ans = []
        for word in strs:
            sortedword = ''.join(sorted(word))
            hash_s[sortedword].append(word)
        for hash_v in hash_s.values():
            ans.append(hash_v)
        return ans