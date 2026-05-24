class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_arr = {}

        for word in strs:

            s_w = "".join(sorted(word))

            if s_w in res_arr:
                res_arr[s_w].append(word)

            else:
                res_arr[s_w] = [word] 

        return list(res_arr.values())