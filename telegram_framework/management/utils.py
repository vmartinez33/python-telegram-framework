import os
import shutil

from packaging.version import parse as parse_version

def copy_template(template_dir, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for item in os.listdir(template_dir):
        src = os.path.join(template_dir, item)
        dst = os.path.join(destination, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

def is_valid_python_version(version):
    return parse_version(version) >= parse_version("3.8")
