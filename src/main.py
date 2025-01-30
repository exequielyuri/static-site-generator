import os
import shutil
import pathlib
from markdown import extract_title, md_to_html_node

def copy_dir(src_path, dst_path):
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
    os.mkdir(dst_path)

    for name in os.listdir(src_path):
        curr_src_path = os.path.join(src_path, name)
        curr_dst_path = os.path.join(dst_path, name)

        if os.path.isfile(curr_src_path):
            shutil.copy(curr_src_path, dst_path)
        else:
            copy_dir(curr_src_path, curr_dst_path)

def generate_page(src_path, tpl_path, dst_path):
    with open(src_path, 'r') as f:
        md = f.read()

    with open(tpl_path, 'r') as f:
        template = f.read()

    title = extract_title(md)
    content = md_to_html_node(md).to_html()
    template = template.replace('{{ Title }}', title).replace(' {{ Content }}', content)

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w') as f:
        f.write(template)

def generate_pages_recursively(src_dir, tpl_path, dst_dir):
    items = os.listdir(src_dir)
    for item in items:
        src_path = os.path.join(src_dir, item)
        path = pathlib.Path(src_path)
        if path.is_file():
            if path.suffix != '.md':
                continue
            curr_dst_path = os.path.join(dst_dir, f'{path.stem}.html')
            generate_page(src_path, tpl_path, curr_dst_path)
        else:
            curr_dst_dir = os.path.join(dst_dir, item)
            generate_pages_recursively(src_path, tpl_path, curr_dst_dir)

def main():
    copy_dir('static', 'public')
    generate_pages_recursively('content', 'template.html', 'public')

main()
