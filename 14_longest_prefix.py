from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    res = []
    for x in zip(*strs):
        if len(set(x)) == 1:
            res.append(x[0])
        else:
            break
    return "".join(res)


strs = ["flower", "flow", "flight"]
strsb = ["flower", "glow", "ilight"]

assert longestCommonPrefix(strs) == "fl"
assert longestCommonPrefix(strsb) == ""
