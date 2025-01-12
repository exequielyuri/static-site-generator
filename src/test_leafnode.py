import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        leaf = LeafNode('p', 'paragraph')
        self.assertEqual(repr(leaf), 'HTMLNode(p, paragraph, None, None)')

    def test_to_html(self):
        tag = 'a'
        value = 'This is a link.'
        props = { 'a': 1, 'b': 2 }
        leaf = LeafNode(tag, value, props)
        self.assertEqual(
                leaf.to_html(),
                f'<{tag} a="1" b="2">{value}</{tag}>'
        )

if __name__ == '__main__':
    unittest.main()
