import re

def extract_md_img(md):
    regex = r'!\[(.*?)\]\((.*?)\)'
    return re.findall(regex, md)

# TODO:
def extract_md_link(md):
    pass
