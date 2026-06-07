class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tMap, window = {}, {}

        for i in t:
            tMap[i] = 1 + tMap.get(i, 0)

        l = 0
        have, need = 0, len(tMap)
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tMap and window[c] == tMap[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        if resLen != float("infinity"):
            return s[l : r + 1]
        else:
            return ""
