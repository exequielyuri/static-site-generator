import unittest
from textnode import TextNode, TextType, text_node_to_html_node

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

class TestTextNodeSplit(unittest.TestCase):
    def test_normal(self):
        node = TextNode('text', TextType.NORMAL)
        split_nodes = node.split('`', TextType.CODE)
        self.assertEqual(split_nodes, [ node ])

    def test_italic(self):
        node = TextNode('text', TextType.ITALIC)
        split_nodes = node.split('`', TextType.CODE)
        self.assertEqual(split_nodes, [ node ])

    def test_bold(self):
        node = TextNode('text', TextType.BOLD)
        split_nodes = node.split('`', TextType.CODE)
        self.assertEqual(split_nodes, [ node ])

    def test_code(self):
        node = TextNode('text', TextType.CODE)
        split_nodes = node.split('`', TextType.BOLD)
        self.assertEqual(split_nodes, [ node ])

    def test_normal_italic(self):
        node = TextNode('a*b*', TextType.NORMAL)
        split_nodes = node.split('*', TextType.ITALIC)
        self.assertEqual(split_nodes, [
            TextNode('a', TextType.NORMAL),
            TextNode('b', TextType.ITALIC)
        ])

    def test_text_bold_text(self):
        node = TextNode('a**b**c', TextType.NORMAL)
        split_nodes = node.split('**', TextType.BOLD)
        self.assertEqual(split_nodes, [
            TextNode('a', TextType.NORMAL),
            TextNode('b', TextType.BOLD),
            TextNode('c', TextType.NORMAL)
        ])

    def test_code_normal_code_normal(self):
        node = TextNode('`a`b`c`d', TextType.NORMAL)
        split_nodes = node.split('`', TextType.CODE)
        self.assertEqual(split_nodes, [
            TextNode('a', TextType.CODE),
            TextNode('b', TextType.NORMAL),
            TextNode('c', TextType.CODE),
            TextNode('d', TextType.NORMAL),
        ])

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_normal(self):
        text_node = TextNode('normal text', TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), 'normal text')

    def test_bold(self):
        text_node = TextNode('bold text', TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<b>bold text</b>')

    def test_italic(self):
        text_node = TextNode('italic text', TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<i>italic text</i>')

    def test_code(self):
        text_node = TextNode('code text', TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<code>code text</code>')

    def test_link(self):
        text_node = TextNode('link text', TextType.LINK, 'link.com')
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<a href="link.com">link text</a>')

    def test_image(self):
        text_node = TextNode('image text', TextType.IMAGE, './image.jpg')
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), '<img alt="image text" src="./image.jpg"></img>')


if __name__ == '__main__':
    unittest.main()

