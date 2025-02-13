from functools import reduce

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError('Child class should implement this.')

    def props_to_html(self):
        if self.props == None:
            raise ValueError('HTMLNode has no properties.')

        props_html_ls = map(lambda x: f' {x[0]}="{x[1]}"', self.props.items())
        return reduce(lambda acc, curr: acc + curr, props_html_ls, '')

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

    def __eq__(self, other):
        return ( self.tag == other.tag
                and self.value == other.value
                and self.children == other.children
                and self.props == other.props )
