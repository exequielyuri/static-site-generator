import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_no_child(self):
        parent = ParentNode('p', None)
        self.assertRaises(ValueError, parent.to_html)

    def test_many_child(self):
        c1 = LeafNode('b', 'c1')
        c2 = LeafNode(None, 'c2')
        c3 = LeafNode('i', 'c3')
        p1 = ParentNode('p', [ c1, c2, c3 ])
        self.assertEqual(p1.to_html(), '<p><b>c1</b>c2<i>c3</i></p>')

    def test_nested_parent(self):
        c1 = LeafNode('b', 'c1')
        p1 = ParentNode('p', [ c1 ])
        p2 = ParentNode('div', [ p1 ])
        self.assertEqual(p2.to_html(), '<div><p><b>c1</b></p></div>')
