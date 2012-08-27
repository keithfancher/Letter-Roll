#!/usr/bin/env python


import unittest

import letterroll as l


class TestGenRegExp(unittest.TestCase):

    def test_single_letter(self):
        re = l.get_reg_expressions("a")
        self.assertEqual(re[0], r"[a-z]*a[a-z]*")

    def test_two_letters(self):
        # sort so we can check for equality more easily
        re = sorted(l.get_reg_expressions("ab"))
        regexp = sorted([r"[a-z]*a[a-z]*b[a-z]*", r"[a-z]*b[a-z]*a[a-z]*"])
        self.assertEqual(re, regexp)

    def test_three_letters(self):
        re = sorted(l.get_reg_expressions("abc"))
        regexp = sorted([r"[a-z]*a[a-z]*b[a-z]*c[a-z]*", r"[a-z]*a[a-z]*c[a-z]*b[a-z]*", r"[a-z]*b[a-z]*a[a-z]*c[a-z]*", r"[a-z]*b[a-z]*c[a-z]*a[a-z]*", r"[a-z]*c[a-z]*a[a-z]*b[a-z]*", r"[a-z]*c[a-z]*b[a-z]*a[a-z]*"])
        self.assertEqual(re, regexp)

    def test_repeated_letters(self):
        re = sorted(l.get_reg_expressions("aa"))
        regexp = sorted([r"[a-z]*a[a-z]*a[a-z]*"])
        self.assertEqual(re, regexp)


if __name__ == "__main__":
    unittest.main()
