import unittest
from markdown import *
from parentnode import ParentNode
from leafnode import LeafNode

class TestMDToBlockType(unittest.TestCase):
    def test_paragraph(self):
        md = 'text'
        block_type = md_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading(self):
        md = '# text'
        block_type = md_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        md = '```code```'
        block_type = md_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)

    def test_u_list(self):
        md = '- a \n * b'
        block_type = md_block_type(md)
        self.assertEqual(block_type, BlockType.U_LIST)

    def test_o_list(self):
        md = '1. a \n 10. b'
        block_type = md_block_type(md)
        self.assertEqual(block_type, BlockType.O_LIST)

class TestMDToHTMLNode(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            md_to_html_node('')

    def test_paragraph(self):
        md = 'text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('p', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_heading_1(self):
        md = '# text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('h1', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_heading_1_no_space(self):
        md = '#text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('h1', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_heading_2(self):
        md = '## text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('h2', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_heading_3(self):
        md = '### text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('h3', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_heading_4(self):
        md = '#### text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('h4', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_heading_5(self):
        md = '##### text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('h5', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_heading_6(self):
        md = '###### text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('h6', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_heading_6_with_extra(self):
        md = '####### text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('h6', [ LeafNode(None, '# text') ]) ])
        self.assertEqual(html_node, expected_node)

    def test_code(self):
        md = '```text```'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html',
                            [ ParentNode('pre',
                                [ ParentNode('code', [ LeafNode(None, 'text') ])
                            ])
                        ])
        self.assertEqual(html_node, expected_node)

    def test_quote(self):
        md = '> text'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [ ParentNode('blockquote', [ LeafNode(None, 'text') ]) ])
        self.assertEqual(html_node, expected_node)

    ##### U_LIST
    # '-a \n *b \n -c'
    #   =>  ParentNode(
    #           tag: 'html',
    #           children: [
    #               ParentNode(
    #                   'ul',
    #                   [
    #                       LeafNode('li', 'a'),
    #                       LeafNode('li', 'b'),
    #                       LeafNode('li', 'c')
    #                   ]
    #           ]
    #       )
    def test_u_list(self):
        md = '-a \n *b \n -c'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [
                            ParentNode('ul',
                                [
                                    ParentNode('li', [ LeafNode(None, 'a') ]),
                                    ParentNode('li', [ LeafNode(None, 'b') ]),
                                    ParentNode('li', [ LeafNode(None, 'c') ])
                                ])
                        ])
        self.assertEqual(html_node, expected_node)

    ##### O_LIST
    # '1.a \n 2.b \n 3.c'
    #   =>  ParentNode(
    #           tag: 'html',
    #           children: [
    #               ParentNode(
    #                   'ol',
    #                   [
    #                       LeafNode('li', 'a'),
    #                       LeafNode('li', 'b'),
    #                       LeafNode('li', 'c')
    #                   ]
    #           ]
    #       )
    def test_o_list(self):
        md = '1. a \n 2.b \n 3.c \n'
        html_node = md_to_html_node(md)
        expected_node = ParentNode('html', [
                            ParentNode('ol',
                                [
                                    ParentNode('li', [ LeafNode(None, 'a') ]),
                                    ParentNode('li', [ LeafNode(None, 'b') ]),
                                    ParentNode('li', [ LeafNode(None, 'c') ])
                                ])
                        ])
        self.assertEqual(html_node, expected_node)
