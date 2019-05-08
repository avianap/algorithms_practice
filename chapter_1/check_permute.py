import unittest

def check_permute(a,b):
    """check is a is a permutation of b

    Args:   
        a (string)
        b (string)
    
    Returns:
        boolean: True is a is a permutation of b
    """
    if len(a) != len(b):
        return False
    else:
        a_dict = {}
        for char in a:
            if char in a_dict:
                a_dict[char] = a_dict[char] + 1
            else:
                a_dict[char] = 1
        for char in b:
            try:
                a_dict[char] = a_dict[char] - 1
                if a_dict[char] < 0:
                    return False
            except:
                return False
        return True

class TestSolution(unittest.TestCase):
    perm_pairs = [('abc','cba'), ('',''), ('hello','leloh')]
    non_perm_pairs = [('abc', 'abc '), ('', ' '), ('hellohello','hellohella')]

    def test_check_permute(self):
        for pair in self.perm_pairs:
            result = check_permute(pair[0],pair[1])
            self.assertTrue(result)
        for pair in self.non_perm_pairs:
            result = check_permute(pair[0],pair[1])
            self.assertFalse(result)

###### SOLUTION

from collections import Counter


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

