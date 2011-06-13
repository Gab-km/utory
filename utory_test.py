# -*- coding: utf-8 -*-

import unittest
import utory

class UtoryTest(unittest.TestCase):
    def base_arguments_are_given(self, input, expected):
        self.assertEqual(input, expected)

case_utory_test = [{'input': 1, 'expected': 1},
                   {'input': 'a', 'expected': 'a'},
                   {'input': [1, 2], 'expected': [1, 2]}]

utory.set_test_dynamicly(UtoryTest,
                         'base_arguments_are_given',
                         case_utory_test)

if __name__ == '__main__':
    unittest.main()
