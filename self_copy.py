__author__ = 'Lesko'

import distutils.core

from_dir = ".\\SD"
to_dir = "H:"

distutils.dir_util.copy_tree(from_dir, to_dir)
