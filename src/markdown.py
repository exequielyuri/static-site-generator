import re
from enum import Enum
from md_helpers import extract_md_blocks
from parentnode import ParentNode
from textnode import md_to_text_nodes

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    U_LIST = 'unordered_list'
    O_LIST = 'ordered_list'

def md_block_type(block):
    block_type = BlockType.PARAGRAPH
    md_lines = list(map(lambda line: line.strip() , block.splitlines()))

    if block.startswith('#'):
        block_type = BlockType.HEADING
    elif block.startswith('```') and block.endswith('```'):
        block_type = BlockType.CODE
    elif block.startswith('>'):
        block_type = BlockType.QUOTE
    elif all(line.startswith(('-', '*')) for line in md_lines):
        block_type = BlockType.U_LIST
    elif all(re.match(r'^\d+\.', line) for line in md_lines):
        block_type = BlockType.O_LIST

    return block_type

def md_to_html_node(md):
    if md == '':
        raise ValueError('MD file does not contain anything')

    blocks = extract_md_blocks(md)
    html_nodes = list(map(block_to_html_node, blocks))
    return ParentNode('html', html_nodes)

def block_to_html_node(block):
    match md_block_type(block):
        case BlockType.PARAGRAPH:
            return ParentNode('p', children_nodes(block))
        case BlockType.HEADING:
            return block_to_heading(block)
        case BlockType.CODE:
            block = re.sub(r'```', '', block)
            return ParentNode('pre', [ ParentNode('code', children_nodes(block)) ])
        case BlockType.QUOTE:
            block = re.sub(r'>\s*', '', block)
            return ParentNode('blockquote', children_nodes(block))
        case BlockType.U_LIST:
            return block_to_u_list(block)
        case BlockType.O_LIST:
            return block_to_o_list(block)

def block_to_heading(block):
    match = re.match(r'(^#{1,6})\s*(.*)', block)

    if match == None:
        raise ValueError('Block is not of type heading.')

    hashes = match.group(1)
    block = match.group(2)
    return ParentNode(f'h{len(hashes)}', children_nodes(block))

def block_to_u_list(block):
    def remove_bullets(item):
        match = re.search(r'[-*]\s*(.*)', item.strip())
        return match and match.group(1)

    items = block.splitlines()
    items = map(remove_bullets, items)
    items = map(lambda item: ParentNode('li', children_nodes(item)), items)
    return ParentNode('ul', list(items))

def block_to_o_list(block):
    def remove_numbering(item):
        match = re.search(r'\d+\.\s*(.*)', item.strip())
        return match and match.group(1)

    items = block.splitlines()
    items = map(remove_numbering, items)
    items = map(lambda item: ParentNode('li', children_nodes(item)), items)
    return ParentNode('ol', list(items))

def children_nodes(block):
    text_nodes = md_to_text_nodes(block)
    children = list(map(lambda tn: tn.to_html_node(), text_nodes))
    return children
