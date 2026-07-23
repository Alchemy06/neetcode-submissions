class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_dict = dict()
        for l in s:
            if (l in s_dict):
                s_dict[l] = s_dict[l] + 1
            else:
                s_dict[l] = 1
        t_dict = dict()
        for l in t:
            if (l in t_dict):
                t_dict[l] = t_dict[l] + 1
            else:
                t_dict[l] = 1
        if s_dict == t_dict:
            return True
        else:
            return False