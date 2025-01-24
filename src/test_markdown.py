import unittest
from markdown import *

class TestMDToBlockType(unittest.TestCase):
    def test_paragraph(self):
        md = 'text'
        block_type = md_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_heading(self):
        md = '# text'
        block_type = md_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        md = '```code```'
        block_type = md_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)

    def test_u_list(self):
        md = '- a \n * b'
        block_type = md_to_block_type(md)
        self.assertEqual(block_type, BlockType.U_LIST)

    def test_o_list(self):
        md = '1. a \n 10. b'
        block_type = md_to_block_type(md)
        self.assertEqual(block_type, BlockType.O_LIST)
