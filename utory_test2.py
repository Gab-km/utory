# -*- coding: utf-8 -*-

import unittest
import utory

class SameArgumentsTest2(unittest.TestCase):
    def base_same_arguments_are_given(self, input, expected):
        self.assertEqual(input, expected)

same_arguments_test = [{'input': 10, 'expected': 10},
                       {'input': 'afro', 'expected': 'afro'},
                       {'input': [1, 2, 3], 'expected': [1, 2, 3]}]

utory.set_test_dynamicly(SameArgumentsTest2,
                         'base_same_arguments_are_given',
                         same_arguments_test)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SameArgumentsTest2)
    unittest.TextTestRunner(verbosity=2).run(suite)
