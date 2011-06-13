# -*- coding: utf-8 -*-

import unittest
import utory

class SameArgumentsTest(unittest.TestCase):
    def base_same_arguments_are_given(self, input, expected):
        self.assertEqual(input, expected)

same_arguments_test = [{'input': 1, 'expected': 1},
                       {'input': 'a', 'expected': 'a'},
                       {'input': [1, 2], 'expected': [1, 2]}]

utory.set_test_dynamicly(SameArgumentsTest,
                         'base_same_arguments_are_given',
                         same_arguments_test)

class DifferentArgumentsTest(unittest.TestCase):
    def base_different_arguments_are_given(self, input, expected):
        self.assertNotEqual(input, expected)

different_arguments_test = [{'input': 1, 'expected': 2},
                            {'input': 'a', 'expected': 'b'},
                            {'input': [1, 2], 'expected': [2, 3]}]

utory.set_test_dynamicly(DifferentArgumentsTest,
                         'base_different_arguments_are_given',
                         different_arguments_test)

# Test methods which name starts with 'test' will not finish successfully.
# You should avoid name starting with 'test' to any test methods
# you want to apply the utory.
#class NameStartsWithTest(unittest.TestCase):
#    def test_name_starts_with_test(self, input, expected):
#        self.assertEqual(input, expected)

#utory.set_test_dynamicly(NameStartsWithTest,
#                         'test_name_starts_with_test',
#                         same_arguments_test)

if __name__ == '__main__':
    unittest.main()
