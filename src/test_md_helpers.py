import unittest
from md_helpers import *

class TestExtractMDImage(unittest.TestCase):
    def test_zero_links(self):
        text = ''
        res = [ ]
        self.assertEqual(extract_md_img(text), res)

    def test_one_link(self):
        text = '![alt](link)'
        res = [ ('alt', 'link') ]
        self.assertEqual(extract_md_img(text), res)

    def test_two_links(self):
        text = '![alt](link) ![alt2](link2)'
        res = [ ('alt', 'link'), ('alt2', 'link2') ]
        self.assertEqual(extract_md_img(text), res)

    def test_links_with_text(self):
        text = 'noise ![alt](link) noise ![alt2](link2) noise'
        res = [ ('alt', 'link'), ('alt2', 'link2') ]
        self.assertEqual(extract_md_img(text), res)

