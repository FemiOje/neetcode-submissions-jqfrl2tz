class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for word in strs:
            charFrequency = [0] * 26

            for letter in word:
                charFrequency[ord(letter) - ord('a')] += 1
            
            result[tuple(charFrequency)].append(word)

        return list(result.values())
        