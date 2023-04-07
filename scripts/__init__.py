import sys
import os
import shutil

os.symlink(os.path.join(os.path.dirname(os.path.realpath(__file__)),"build"),os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'build'))

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
