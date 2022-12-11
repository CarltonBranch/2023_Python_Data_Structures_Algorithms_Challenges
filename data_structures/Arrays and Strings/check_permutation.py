import unittest
"""Problem statement: Given two strings, write a method to decide if one is a permutation of the other
    """


def process_character(hash_table: dict, letter: chr):
    """Helper function to insert characters/character counts into a dictionary

    Args:
        hash_table (dict): dictionary (mutated by reference)
        letter (chr): character
    """
    if letter in hash_table:
        hash_table[letter] += 1
    else:
        hash_table[letter] = 0


def check_permutation(wordA: str, wordB: str):
    """Checks whether or not both strings have the same type and quantity of 
    each character

    Args:
        wordA (str): string to compare
        wordB (str): string to compare

    Returns:
        Boolean: True if wordA is permutation of WordB
    """
    # to be permutation candidates, both strings must have the same number of characters
    if len(wordA) != len(wordB):
        return False

    # sorting both words and then comparing character by character would be (n log n + n = n log n)
    # putting then into two hash tables and comparing hash tables would be (n + n = n)
    hashA = {}
    hashB = {}
    for index in range(len(wordA)):
        process_character(hashA, wordA[index])
        process_character(hashB, wordB[index])

    # if the resulting sets of unique characters do not have the same length, the underlying words are not permutations
    if len(hashA) != len(hashB):
        return False

    # iterate through each character in the tables to see if they have matching values
    for element in hashA.items():
        if hashB.get(element[0]) is None:
            return False
        if element[1] != hashB[element[0]]:
            return False

    return True


# test cases
class TestIsUniqueMethods(unittest.TestCase):

    def test_should_be_true(self):
        self.assertTrue(check_permutation(
            'Abcdefghijklmnopa', 'Abcdefghijklmnopa'))
        self.assertTrue(check_permutation(
            'abcdefghijklmnop', 'ponmlkjihgfedcab'))
        self.assertTrue(check_permutation('c', 'c'))
        self.assertTrue(check_permutation('', ''))

    def test_should_be_false(self):
        self.assertFalse(check_permutation('abcdefga', 'abcdefgA'))
        self.assertFalse(check_permutation(
            'abrdsedtuitjkg', 'abrdsedtuitjk g'))
        self.assertFalse(check_permutation(
            'abcdefghijklmnopqrstuvwza', 'abcdefghijklmnopqrstuvwz'))
        self.assertFalse(check_permutation('A', 'a'))


if __name__ == '__main__':
    unittest.main()
