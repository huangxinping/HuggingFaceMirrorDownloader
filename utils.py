import sys
import subprocess


def is_library_installed(library_name):
    try:
        __import__(library_name)
        return True
    except ImportError:
        return False


def install_library(library_name, retry_numbers=0):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
    except subprocess.CalledProcessError:
        if retry_numbers < 10:
            install_library(library_name, retry_numbers + 1)


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    return False
