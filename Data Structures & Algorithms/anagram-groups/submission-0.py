from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anahash = defaultdict(list)
        for string in strs:
            alphabet = [0] * 26
            for char in string:
                alphabet[ord(char) - 97] += 1
            anahash[tuple(alphabet)].append(string)
        return list(anahash.values())