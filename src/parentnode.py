from htmlnode import HTMLNode
from functools import reduce

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.children == None:
            raise ValueError('ParentNode has no children.')
        if self.tag == None:
            raise ValueError('ParentNode has no tag.')

        child_html_ls = map(lambda child: child.to_html(), self.children)
        accumulated_child_html = reduce(lambda acc, curr: acc + curr, child_html_ls, '')
        return f'<{self.tag}>{accumulated_child_html}</{self.tag}>'

