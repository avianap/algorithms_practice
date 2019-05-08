import unittest

def is_unique(string):
    """check is all the characters in a string are unique

    Args:
        string (string): string to check 
    
    Returns:
        Boolean: True is all the characters are unique
    """
    string_dict = {}
    for character in string:
        if character not in string_dict:
            string_dict[character] = 1
        else:
            return False
    return True


def is_unique_2(string):
    """check if a string is unique without using any additional data structures

    Args:   
        string (string): string to check for unique chars

    Returns:
        Boolean: True is all the characters are unique
    """
    for i in range(0,len(string)-1):
        for j in range(i+1,len(string)):
            if string[i] == string[j]:
                return False
    return True

class Test(unittest.TestCase):
    test_true_strings = ['abcd','12345','']
    test_false_strings = ['aaaa', '  ', '1231']

    def test_is_unique(self):
        for test_string in self.test_true_strings:
            result = is_unique(test_string)
            self.assertTrue(result)
        for test_string in self.test_false_strings:
            result = is_unique(test_string)
            self.assertFalse(result)

    def test_is_unique_2(self):
        for test_string in self.test_true_strings:
            result = is_unique_2(test_string)
            self.assertTrue(result)
        for test_string in self.test_false_strings:
            result = is_unique_2(test_string)
            self.assertFalse(result)
        

####### SOLUTION

def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

class TestSolution(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()

