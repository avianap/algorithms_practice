import unittest

class Solution:
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        while len(strs) >= 2:
            string_1 = strs.pop(0)
            string_2 = strs.pop(0)
            strs.append(self.helperFunction(string_1, string_2))
        return strs[0]
    
    def helperFunction(self, string_1, string_2):
        common = ""
        if (string_1 == "") | (string_2 == ""):
            return common
        else:
            for letter_1, letter_2 in zip(string_1, string_2):
                if letter_1 == letter_2:
                    common = common + letter_1
                else:
                    return common
            return common
                    
class TestSolution(unittest.TestCase):
    S = Solution()

    def test_longestCommonPrefix_blanks(self):
        actual = self.S.longestCommonPrefix(["a","b",""])
        self.assertEqual(actual, "")

    def test_longestCommonPrefix_partial(self):
        actual = self.S.longestCommonPrefix(["a","abc","aaa"])
        self.assertEqual(actual, "a")

    def test_longestCommonPrefix_total(self):
        actual = self.S.longestCommonPrefix(["abc","abc","abc"])
        self.assertEqual(actual, "abc")



if __name__ == "__main__":
    unittest.main()
