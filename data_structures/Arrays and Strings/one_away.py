import unittest


def one_away(word_a: str, word_b: str):
    """  Returns True if wordA is identical to wordB minus the difference of one character  """
   # if the differnce between word lengths is greater than 1
   #    => return False
   # if the difference between word lengths is equal to 1
   #    => all characters of smaller must be the same as the larger
   # if the differnce between word lengths is zero
   #    => all character counts must be the same expect for 1

    length_difference = abs(len(word_a) - len(word_b))

    # if the difference between word lengths is greater than 1, return False
    if length_difference > 1:
        return False

    # if the difference between word lengths, all characters of smaller must be same as larger
    if length_difference == 1:
        longer = shorter = ""
        if len(word_a) > len(word_b):
            longer = word_a
            shorter = word_b
        else:
            longer = word_b
            shorter = word_a
        longer_map = process_word(longer)
        shorter_map = process_word(shorter)
        for item in shorter_map.items():
            # the character count in shorter word must be present and less than or equal to that character in longer
            check = longer_map.get(item[0])
            if check is None:
                return False
            elif item[1] > longer_map[item[0]]:
                return False
        return True
    # if the words are the sanme lengths, all character counts must match or except for one character or count (by 1)
    if length_difference == 0:
        map_a = process_word(word_a)
        map_b = process_word(word_b)
        change_count = 0

        for item in map_a.items():
            check_b = map_b.get(item[0])
            if check_b is None:
                # this character has been removed from the other string
                # if the character count is greater than 1 this is not a one-away permutation
                if item[1] != 1:
                    return False
                else:
                    change_count += 1
            else:
                # if this character appears the same number of times as in the other string - nothing to do here
                if item[1] == check_b:
                    continue
                else:
                    # if the difference between these characters is greater than 1 - can't be a one-away permutation
                    if abs(item[1] - check_b) > 1:
                        return False
                    else:
                        # if the difference between them is 1, count this as another 1 away change
                        # (there can only be 0 or 1 for a valid pair)
                        change_count += 1

    return True and change_count <= 1


def process_word(word: str):
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result


# test cases
class TestIsUniqueMethods(unittest.TestCase):

    def test_should_be_true(self):
        self.assertTrue(one_away('play', 'ply'))
        self.assertTrue(one_away('play', 'plays'))
        self.assertTrue(one_away('playerplayer', 'playerplaye'))
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertTrue(one_away('pale', 'play'))

    def test_should_be_false(self):
        self.assertFalse(one_away('play', 'player'))
        self.assertFalse(one_away('play', 'pl'))
        self.assertFalse(one_away('play', 'plyyy'))
        self.assertFalse(one_away('play', 'plr'))
        self.assertFalse(one_away('play', 'bake'))
        self.assertFalse(one_away('pale', 'plyy'))


if __name__ == '__main__':
    unittest.main()
