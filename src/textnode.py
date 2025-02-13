from enum import Enum
from leafnode import LeafNode
from md_helpers import extract_md_img, extract_md_link
from functools import reduce

class TextType(Enum):
    NORMAL = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return ( self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url )

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

    def split(self, delim, text_type):
        if self.text_type != TextType.NORMAL:
            return [ self ]

        nodes = []
        texts = self.text.split(delim)
        for idx in range(0, len(texts)):
            if texts[idx] == '': continue
            if idx%2 == 0: nodes.append(TextNode(texts[idx], TextType.NORMAL))
            else: nodes.append(TextNode(texts[idx], text_type))
        return nodes

    def split_img_nodes(self):
        if self.text_type != TextType.NORMAL:
            return [ self ]

        imgs = extract_md_img(self.text)
        if len(imgs) == 0:
            return [ self ]

        nodes = []
        curr_text = self.text
        for img in imgs:
            img_md = f'![{img[0]}]({img[1]})'
            texts = curr_text.split(img_md, 1)
            if texts[0] != '': nodes.append(TextNode(texts[0], TextType.NORMAL))
            nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
            curr_text = texts[1]
        if curr_text != '': nodes.append(TextNode(curr_text, TextType.NORMAL))

        return nodes

    def split_link_nodes(self):
        if self.text_type != TextType.NORMAL:
            return [ self ]

        links = extract_md_link(self.text)
        if len(links) == 0:
            return [ self ]

        nodes = []
        curr_text = self.text
        for link in links:
            link_md = f'[{link[0]}]({link[1]})'
            texts = curr_text.split(link_md, 1)
            if texts[0] != '': nodes.append(TextNode(texts[0], TextType.NORMAL))
            nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            curr_text = texts[1]
        if curr_text != '': nodes.append(TextNode(curr_text, TextType.NORMAL))

        return nodes

    def to_html_node(self):
        html_node = LeafNode(None, '')

        match self.text_type:
            case TextType.NORMAL:
                html_node = LeafNode(None, self.text)
            case TextType.BOLD:
                html_node = LeafNode('b', self.text)
            case TextType.ITALIC:
                html_node = LeafNode('i', self.text)
            case TextType.CODE:
                html_node = LeafNode('code', self.text)
            case TextType.LINK:
                props = { 'href': self.url }
                html_node = LeafNode('a', self.text, props)
            case TextType.IMAGE:
                props = { 'alt': self.text, 'src': self.url }
                html_node = LeafNode('img', None, props)
            case _:
                raise ValueError('Invalid text type.')

        return html_node

def md_to_text_nodes(md):
    nodes = [ TextNode(md, TextType.NORMAL) ]
    nodes = reduce(lambda acc, curr: acc + curr.split('**', TextType.BOLD), nodes, [])
    nodes = reduce(lambda acc, curr: acc + curr.split('*', TextType.ITALIC), nodes, [])
    nodes = reduce(lambda acc, curr: acc + curr.split('`', TextType.CODE), nodes, [])
    nodes = reduce(lambda acc, curr: acc + curr.split_img_nodes(), nodes, [])
    nodes = reduce(lambda acc, curr: acc + curr.split_link_nodes(), nodes, [])
    return nodes
