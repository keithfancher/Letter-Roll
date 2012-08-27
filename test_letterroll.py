#!/usr/bin/env python


import unittest

import letterroll as l


class TestGenRegExp(unittest.TestCase):

    def test_single_letter(self):
        re = l.get_reg_expressions("a")
        self.assertEqual(re[0], r"[a-z]*a[a-z]*")


if __name__ == "__main__":
    unittest.main()
