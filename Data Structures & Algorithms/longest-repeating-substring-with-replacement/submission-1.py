class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, result, curr_highest = 0, 0, 0
        char_set = {}

        for r in range(len(s)):
            char_set[s[r]] = char_set.get(s[r], 0) + 1
            curr_highest = max(curr_highest, char_set[s[r]])

            if r - l + 1 - curr_highest > k:
                char_set[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result
        