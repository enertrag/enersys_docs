import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Enersys'
extensions = ['myst_parser']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'
html_theme = 'sphinx_rtd_theme'
