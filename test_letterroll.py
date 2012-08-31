#!/usr/bin/env python


import unittest

import letterroll as l
import web_letterroll as w


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


class TestWordMatchesRegExpList(unittest.TestCase):
    def test_one_to_one(self):
        word = "a"
        regexp_list = [r"a"]
        self.assertTrue(l.word_matches_regexp_list(word, regexp_list))

    def test_one_to_many(self):
        word = "giantboner"
        regexp_list = [r"asdfsdafsd", r"boner", r"cray cray"]
        self.assertTrue(l.word_matches_regexp_list(word, regexp_list))

    def test_should_fail(self):
        word = "giantboner"
        regexp_list = [r"asdfsdafsd", r"bnr", r"cray cray"]
        self.assertFalse(l.word_matches_regexp_list(word, regexp_list))


class TestWebInterface(unittest.TestCase):

    def setUp(self):
        w.app.config['TESTING'] = True
        self.app = w.app.test_client()

    def test_index_exists(self):
        r = self.app.get('/')
        assert "Enter the letters you've rolled" in r.data
        assert r.status_code == 200

    def test_url_request(self):
        """Passing your letters directly to the URL should work"""
        r = self.app.get('/results/ffff')
        assert "riffraff" in r.data
        assert r.status_code == 200

    def test_post_data(self):
        """Sending your letters as POST data should work too!"""
        r = self.app.post('/', data=dict(q='ffff'), follow_redirects=True)
        assert "riffraff" in r.data
        assert r.status_code == 200

    def test_empty_string_passed(self):
        """Passing an empty string should redirect to index"""
        r = self.app.get('/results/')
        assert "Enter the letters you've rolled" in r.data
        assert r.status_code == 200

    def test_dumb_string_returns_no_results(self):
        r = self.app.get('/results/xxx')
        assert "No matches" in r.data
        assert r.status_code == 200

    def test_nonsense_returns_404(self):
        r = self.app.get('/asdfasdfsdaf')
        assert r.status_code == 404

    def test_resulsts_case_insensitive(self):
        r = self.app.get('/results/fFfF')
        assert "riffraff" in r.data
        assert r.status_code == 200


if __name__ == "__main__":
    unittest.main()
