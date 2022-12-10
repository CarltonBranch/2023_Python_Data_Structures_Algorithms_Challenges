import unittest
"""Problem statement: "Implement an algorithm to determine if a string has all unique characters? 
       What if you can't use additional data structures?
    """


def is_unique(word: str):
    """Checks string input to see if all letters are unique to the string
    Args:
        word (str): string to be analyzed
    Returns:
        _type_: boolean
        False - if any letter has at least one duplicate
        True - if all included letters appear only once or if there are no letters
    """
    # handle special cases of zero letters and one letter
    if len(word) <= 2:
        return True

    # to avoid using a hash table, sort the word (0 n log n )
    sorted_word = sorted(word)

    # check that each letter a
    for index, letter in enumerate(sorted_word):
        if letter == sorted_word[index - 1]:
            return False
    return True


# test cases
class TestIsUniqueMethods(unittest.TestCase):

    def test_should_be_true(self):
        self.assertTrue(is_unique('Abcdefghijklmnopa'))
        self.assertTrue(is_unique('ca'))
        self.assertTrue(is_unique('c'))
        self.assertTrue(is_unique(''))

    def test_should_be_false(self):
        self.assertFalse(is_unique('abcdefga'))
        self.assertFalse(is_unique('abrdsedtuitjkg'))
        self.assertFalse(is_unique('abcdefghijklmnopqrstuvwza'))
        self.assertFalse(is_unique('AbcdefghijklmnopA'))


if __name__ == '__main__':
    unittest.main()
git
