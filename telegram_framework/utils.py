from packaging.version import parse as parse_version

def is_valid_python_version(version):
    return parse_version(version) >= parse_version("3.8")
