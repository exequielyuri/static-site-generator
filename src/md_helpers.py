import re

def extract_md_img(md):
    regex = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'
    return re.findall(regex, md)

def extract_md_link(md):
    regex = r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    return re.findall(regex, md)

def extract_md_blocks(md):
    blocks = md.split('\n\n')
    blocks = map(lambda block: block.strip(), blocks)
    blocks = filter(lambda block: block != '', blocks)
    return list(blocks)

