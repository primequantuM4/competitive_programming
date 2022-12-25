class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # use a dictionary for string s and then traverse t and check if it is in the dict
        # reason we aren't using a set is cause if there's any reapting value it just assumes
        #it isn't added
        elements_in_s = Counter(s)
        for i in t:
            if i not in elements_in_s or elements_in_s[i] == 0:
                return i
            elements_in_s[i] -= 1
        return ""
