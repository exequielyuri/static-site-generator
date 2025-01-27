import os
import shutil
from textnode import TextNode, TextType

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

def main():
    copy_dir('static', 'public')


main()
