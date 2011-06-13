# -*- coding: utf-8 -*-

def create_test(base_method_name, dct):
    def do_assertion(obj):
        input = dct['input']
        expected = dct['expected']
        exec("obj." + base_method_name + \
             "(input=input, expected=expected)")
    return do_assertion

def set_test_dynamicly(target_class, base_method_name, dctList):
    for dct in dctList:
        test_method = create_test(base_method_name, dct)
        hs = hash(repr(dct))
        if hs < 0:
            hs = -hs
        test_method.__name__ = 'test' + base_method_name[4:] + \
                               '@' + str(hs)
        setattr(target_class, test_method.__name__, test_method)
