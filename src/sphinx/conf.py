
# -- Project information -----------------------------------------------------
project = 'mypackage'
author = 'Yohey Ishizu'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_show_copyright = False
html_show_sourcelink = False

# -- Options for todo extension ----------------------------------------------
todo_include_todos = True
