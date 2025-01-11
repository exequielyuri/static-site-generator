import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_default_properties(self):
        node = HTMLNode()
        self.assertEqual(repr(node), 'HTMLNode(None, None, None, None)')

    def test_repr(self):
        node_props = { 'a': 'b' }
        node = HTMLNode('a', 'this is a link', None, node_props)
        self.assertEqual(repr(node), "HTMLNode(a, this is a link, None, {'a': 'b'})")

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode()
        self.assertRaises(ValueError, node.props_to_html)

        node = HTMLNode(props={ 'a': 'b', 'c': 'd' })
        self.assertEqual(node.props_to_html(), ' a="b" c="d"')


if __name__ == '__main__':
    unittest.main()
