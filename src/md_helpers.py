import re

def extract_md_img(md):
    regex = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'
    return re.findall(regex, md)

def extract_md_link(md):
    regex = r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    return re.findall(regex, md)
