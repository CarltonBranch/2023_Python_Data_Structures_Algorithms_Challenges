"""Problem statement: 'Write a method to replace all spaces in a string with '%20'
        You may assume that the string has sufficient space at the end to hold the additional
        characters.
    """
import unittest


def url_ify(url: str):
    """Returns a new string where all spaces are replaced with '%20'
    Args:
        url (str): _description_
    Returns:
        _type_: _description_
    """
    result = ""
    # remove any whitespace around the url to be processed
    url = url.strip()
    # note this could be done with the replace function: string.replace(oldvalue, newvalue, optional_count) - CB
    for letter in url:
        if letter == ' ':
            result += '%20'
        else:
            result += letter

    return result


# test cases
class TestURLifymethod(unittest.TestCase):
    """Testing class
    Args:
        unittest (_type_): _description_
    """

    def test(self):
        """Unit test cases
        """
        self.assertEqual(
            url_ify('http://www.the wonderful world of disney.com'), 'http://www.the%20wonderful%20world%20of%20disney.com')
        self.assertEqual(
            url_ify('      http://www.the wonderful world of disney.com            '), 'http://www.the%20wonderful%20world%20of%20disney.com')


if __name__ == '__main__':
    unittest.main()
