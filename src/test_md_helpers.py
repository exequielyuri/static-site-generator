import unittest
from md_helpers import *

class TestExtractMDImage(unittest.TestCase):
    def test_zero_img(self):
        text = ''
        res = [ ]
        self.assertEqual(extract_md_img(text), res)

    def test_one_img(self):
        text = '![alt](link)'
        res = [ ('alt', 'link') ]
        self.assertEqual(extract_md_img(text), res)

    def test_two_imgs(self):
        text = '![alt](link) ![alt2](link2)'
        res = [ ('alt', 'link'), ('alt2', 'link2') ]
        self.assertEqual(extract_md_img(text), res)

    def test_imgs_with_noise(self):
        text = 'noise ![alt](link) noise ![alt2](link2) [alt3](link3)'
        res = [ ('alt', 'link'), ('alt2', 'link2') ]
        self.assertEqual(extract_md_img(text), res)

    def test_imgs_with_irreg(self):
        text = 'noise ![alt](link) noise ![[alt2](link2) ![alt3](l(ink3)'
        res = [ ('alt', 'link') ]
        self.assertEqual(extract_md_img(text), res)

class TestExtractMDLink(unittest.TestCase):
    def test_zero_link(self):
        text = ''
        res = [ ]
        self.assertEqual(extract_md_link(text), res)

    def test_one_link(self):
        text = '[alt](link)'
        res = [ ('alt', 'link') ]
        self.assertEqual(extract_md_link(text), res)

    def test_two_links(self):
        text = '[alt](link) [alt2](link2)'
        res = [ ('alt', 'link'), ('alt2', 'link2') ]
        self.assertEqual(extract_md_link(text), res)

    def test_links_with_noise(self):
        text = 'noise [alt](link) noise ![alt2](link2) [alt3](link3)'
        res = [ ('alt', 'link'), ('alt3', 'link3') ]
        self.assertEqual(extract_md_link(text), res)

    def test_links_with_irreg(self):
        text = 'noise [alt](link) noise [al]t2](link2) [alt3](l(ink3)'
        res = [ ('alt', 'link') ]
        self.assertEqual(extract_md_link(text), res)

if __name__ == '__main__':
    unittest.main()
