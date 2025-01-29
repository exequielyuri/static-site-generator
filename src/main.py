import os
import shutil
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

def generate_page(src_path, template_path, dst_path):
    with open(src_path, 'r') as f:
        md = f.read()

    with open(template_path, 'r') as f:
        template = f.read()

    title = extract_title(md)
    content = md_to_html_node(md).to_html()
    template = template.replace('{{ Title }}', title).replace(' {{ Content }}', content)

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w') as f:
        f.write(template)

def main():
    copy_dir('static', 'public')
    generate_page('content/index.md', 'template.html', 'public/index.html')

main()
