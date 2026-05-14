class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        b = False
        start = strs[0]
        for l in range(len(start)):
            for i in strs[1:]:
                rl = start[l]
                try:
                    ml = i[l]
                except IndexError:
                    b = True
                    break
                if ml == rl:
                    continue
                    # go to the next word to compare
                else:
                    b = True
                    break
                    # break out completely
            else:
                j += 1
                continue
            if b:
                break
        if j == 0:
            return ""
        else:
            return start[:j]
