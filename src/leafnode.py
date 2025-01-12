from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not hasattr(self, 'value'):
            raise ValueError('LeafNode has no value')

        return (self.value if self.tag==None
                else f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>')
