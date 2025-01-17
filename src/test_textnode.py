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
        html_node = text_node.to_html_node()
        self.assertEqual(html_node.to_html(), 'normal text')

    def test_bold(self):
        text_node = TextNode('bold text', TextType.BOLD)
        html_node = text_node.to_html_node()
        self.assertEqual(html_node.to_html(), '<b>bold text</b>')

    def test_italic(self):
        text_node = TextNode('italic text', TextType.ITALIC)
        html_node = text_node.to_html_node()
        self.assertEqual(html_node.to_html(), '<i>italic text</i>')

    def test_code(self):
        text_node = TextNode('code text', TextType.CODE)
        html_node = text_node.to_html_node()
        self.assertEqual(html_node.to_html(), '<code>code text</code>')

class TestTextNodeToImages(unittest.TestCase):
    def test_not_normal(self):
        node = TextNode('text', TextType.BOLD)
        nodes = node.split_img_nodes()
        self.assertEqual(nodes, [ node ])

    def test_one_img(self):
        node = TextNode('![alt](link)', TextType.NORMAL)
        nodes = node.split_img_nodes()
        self.assertEqual(nodes, [ TextNode('alt', TextType.IMAGE, 'link') ])

    def test_img_no_alt(self):
        node = TextNode('![](link)', TextType.NORMAL)
        nodes = node.split_img_nodes()
        self.assertEqual(nodes, [ TextNode('', TextType.IMAGE, 'link') ])

    def test_img_no_link(self):
        node = TextNode('![alt]()', TextType.NORMAL)
        nodes = node.split_img_nodes()
        self.assertEqual(nodes, [ TextNode('alt', TextType.IMAGE, '') ])

    def test_imgs_with_noise(self):
        node = TextNode('a ![a1](l1) b ![a2](l2) [t1](h1)', TextType.NORMAL)
        nodes = node.split_img_nodes()
        self.assertEqual(nodes, [
            TextNode('a ', TextType.NORMAL),
            TextNode('a1', TextType.IMAGE, 'l1'),
            TextNode(' b ', TextType.NORMAL),
            TextNode('a2', TextType.IMAGE, 'l2'),
            TextNode(' [t1](h1)', TextType.NORMAL),
        ])

class TestTextNodeToLinks(unittest.TestCase):
    def test_not_normal(self):
        node = TextNode('text', TextType.BOLD)
        nodes = node.split_link_nodes()
        self.assertEqual(nodes, [ node ])

    def test_one_link(self):
        node = TextNode('[text](href)', TextType.NORMAL)
        nodes = node.split_link_nodes()
        self.assertEqual(nodes, [ TextNode('text', TextType.LINK, 'href') ])

    def test_link_no_text(self):
        node = TextNode('[](href)', TextType.NORMAL)
        nodes = node.split_link_nodes()
        self.assertEqual(nodes, [ TextNode('', TextType.LINK, 'href') ])

    def test_link_no_href(self):
        node = TextNode('[text]()', TextType.NORMAL)
        nodes = node.split_link_nodes()
        self.assertEqual(nodes, [ TextNode('text', TextType.LINK, '') ])

    def test_links_with_noise(self):
        node = TextNode('a [t1](h1) b [t2](h2) ![a1](l1)', TextType.NORMAL)
        nodes = node.split_link_nodes()
        self.assertEqual(nodes, [
            TextNode('a ', TextType.NORMAL),
            TextNode('t1', TextType.LINK, 'h1'),
            TextNode(' b ', TextType.NORMAL),
            TextNode('t2', TextType.LINK, 'h2'),
            TextNode(' ![a1](l1)', TextType.NORMAL),
        ])

if __name__ == '__main__':
    unittest.main()

