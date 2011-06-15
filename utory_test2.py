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

class DifferentArgumentsTest2(unittest.TestCase):
    def base_different_arguments_are_given(self, input, expected):
        self.assertNotEqual(input, expected)

different_arguments_test = [{'input': 10, 'expected': 20},
                            {'input': 'afro', 'expected': 'bobo'},
                            {'input': [1, 2, 3], 'expected': [2, 3, 4, 5]}]

utory.set_test_dynamicly(DifferentArgumentsTest2,
                         'base_different_arguments_are_given',
                         different_arguments_test)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite_same = loader.loadTestsFromTestCase(SameArgumentsTest2)
    suite_diff = loader.loadTestsFromTestCase(DifferentArgumentsTest2)
    all_suite = unittest.TestSuite([suite_same, suite_diff])
    unittest.TextTestRunner(verbosity=2).run(all_suite)
