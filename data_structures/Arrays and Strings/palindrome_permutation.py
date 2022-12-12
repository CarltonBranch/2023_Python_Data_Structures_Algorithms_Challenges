"""_summary_
    Given a string write a function to check if it is a permutation of a palindrome.
    A palindrome is a word that is the same forward and backwards. A permutation
    is an rearrangement of letters. Non dictionary words are valid.
    You do not need to generate all permutations.
    """
import unittest


def palindrome_permutation(word: str):
    """Returns true if word could be a palindrome

    Args:
        word (str): string to be analyzed

    Returns:
        True:
            if word has 0 or 1 character
            if word has three or more characters where only one character appears once and all
            other characters appear a multiple of two times

    """
    # remove whitespaces from input
    word_input = word.strip()
    word_input = word_input.replace(' ', "")

    # process word into occurrence map by character
    if len(word_input) <= 1:
        return True
    letter_dict = {}
    for letter in word_input:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    # check occurence map: all characters must appear in multiples of 2
    # and only one character can appear once

    singleton_found = False

    for item in letter_dict.items():
        current_val = item[1]
        # handle the single occurence of a character
        if current_val == 1 and singleton_found is False:
            singleton_found = True
            continue

        # if there is more than 1 character with 1 occurrence - not a potential palindrome
        # if there is a character with an odd number of occurrences - not a potential palindrome
        if current_val % 2 != 0 or current_val == 1:
            return False

    return True


# test cases
class TestPalindromePermutation(unittest.TestCase):
    def test_should_be_true(self):
        self.assertTrue(palindrome_permutation('taco cat'))
        self.assertTrue(palindrome_permutation('lol'))
        self.assertTrue(palindrome_permutation('oll'))
        self.assertTrue(palindrome_permutation('t a c o c a t'))
        self.assertTrue(palindrome_permutation('   kaya    k'))
        self.assertTrue(palindrome_permutation('divideerr'))
        self.assertTrue(palindrome_permutation('damam'))
        self.assertTrue(palindrome_permutation('car race'))

    def test_should_be_false(self):
        self.assertFalse(palindrome_permutation('carlton'))
        self.assertFalse(palindrome_permutation('helo'))
        self.assertFalse(palindrome_permutation('aabbccdd'))
        self.assertFalse(palindrome_permutation('Madam'))


if __name__ == '__main__':
    unittest.main()
