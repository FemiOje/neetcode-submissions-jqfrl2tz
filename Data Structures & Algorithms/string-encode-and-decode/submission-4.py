class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        last_pos = 0

        while last_pos < len(s):
            new_pos = last_pos

            while s[new_pos] != "#":
                new_pos += 1

            word_length = int(s[last_pos:new_pos])
            new_word = ""

            for i in range(word_length):
                new_word += s[new_pos + i + 1]

            decoded.append(new_word)
            last_pos = new_pos + word_length + 1

        return decoded