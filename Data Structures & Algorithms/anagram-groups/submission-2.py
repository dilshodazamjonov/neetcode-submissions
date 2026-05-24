from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_arr = defaultdict(list)

        for word in strs:

            s_w = "".join(sorted(word))

            res_arr[s_w].append(word)

        return list(res_arr.values())