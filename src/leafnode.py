from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not hasattr(self, 'value'):
            raise ValueError('LeafNode has no value.')
        if self.tag == None:
            return self.value

        props_html = '' if self.props==None else self.props_to_html()
        return f'<{self.tag}{props_html}>{self.value or ''}</{self.tag}>'
