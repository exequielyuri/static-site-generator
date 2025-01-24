from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    U_LIST = 'unordered_list'
    O_LIST = 'ordered_list'

def md_to_block_type(md):
    block_type = BlockType.PARAGRAPH
    md_lines = list(map(lambda line: line.strip() , md.splitlines()))

    if md.startswith('#'):
        block_type = BlockType.HEADING
    elif md.startswith('```'):
        block_type = BlockType.CODE
    elif md.startswith('>'):
        block_type = BlockType.QUOTE
    elif all(line.startswith(('-', '*')) for line in md_lines):
        block_type = BlockType.U_LIST
    elif all(re.match(r'^\d+\.', line) for line in md_lines):
        block_type = BlockType.O_LIST

    return block_type
