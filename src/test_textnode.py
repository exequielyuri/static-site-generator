import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_neq(self):
        node1 = TextNode('Text node', TextType.NORMAL)
        node2 = TextNode('Text node', TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode('Text node', TextType.NORMAL, 'boot.dev')
        self.assertEqual(repr(node), 'TextNode(Text node, normal, boot.dev)')

    def test_repr_without_url(self):
        node = TextNode('Text node', TextType.NORMAL)
        self.assertEqual(repr(node), 'TextNode(Text node, normal, None)')


if __name__ == '__main__':
    unittest.main()

