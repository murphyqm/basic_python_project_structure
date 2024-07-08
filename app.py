import streamlit as st
import re

st.title('Basic Python Project Structure')

st.write("This webapp creates customised code snippets to help you set up a Python package project.",
"First, look through the **Picking a project name** tab and decide on a name for your Python package.",
"Then, go to the **Project details** tab and fill in information for your project.",
"Then, you can generate a sensible project folder structure using the `bash` scripts in the tab **Folder Structure**.",
"You can build your Python package using the generated `pyproject.toml` template in the **pyproject.toml** tab." )

# font_css = """
# <style>
# button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
#   font-size: 18px;
# }
# </style>
# """

# st.markdown("""
# <style>

# 	.stTabs [data-baseweb="tab-list"] {
# 		gap: 5px;
#     }

# 	.stTabs [data-baseweb="tab"] {
# 		height: 50px;
#         white-space: pre-wrap;
# 		background-color: #F0F2F6;
# 		border-radius: 4px 4px 0px 0px;
# 		gap: 5px;
# 		padding-top: 10px;
# 		padding-bottom: 10px;
#     }

# 	.stTabs [aria-selected="true"] {
#   		background-color: #FFFFFF;
# 	}

# </style>""", unsafe_allow_html=True)

# st.write(font_css, unsafe_allow_html=True)

tablist = ["\u2001 Picking a project name \u2001", "\u2001 Project details \u2001", "\u2001 Folder structure \u2001", "\u2001 pyproject.toml \u2001", "\u2001 Build docs \u2001"]

intro, tab0, tab1, tab2, tab3 = st.tabs(tablist)

with intro:
    st.header("Basic information on picking a project name.")
    st.markdown(
        """
        Picking a sensible project and package name can be challenging. There are a few rules to follow:
        - For your Python package name, stick to just lowercase letters and underscores. No spaces! No hyphens!
        - Make your repository name for the project the same as the package name, again all lowercase, but use hyphens instead of underscores. This is not a rule, but is a nice [convention](https://github.com/GoldenbergLab/naming-and-documentation-conventions)]
        - If you plan on publishing your package on PyPI (so you can install with pip), check that there are no packages with the same name!
        """
        )
    test_name = st.text_input("Test your name here:", "package_name")

    if re.search(r"\s", test_name):
        st.write("Remove spaces!")
    if re.search(r"-", test_name):
        st.write("Remove hyphens!")
    no_spaces = re.sub('\s+', '_', test_name)
    no_hyphens = re.sub('-', '_', no_spaces)
    just_hyphens = re.sub('_', '-', no_hyphens)

    st.write(f"Your package name: `{no_hyphens}`")
    st.write(f"Your repository (folder) name: `{just_hyphens}`")

with tab0:
    project_name = st.text_input("Enter your package name (lowercase letters and underscores only!):", "example_package")
    project_name = re.sub('\s+', '_', project_name)
    project_name = re.sub('-', '_', project_name)

    repo_name = re.sub('_', '-', project_name)

    st.write(f"Your package name: `{project_name}`. If this doesn't look right, please change your input!")
    st.write(f"You can call your git repository `{repo_name}` for consistency!")

    author_name = st.text_input("Enter the author's full name:", "Author Full Name")

    author_email = st.text_input("Enter the author's email:", "authors_email@goes_here.ie")

    version = st.text_input("Enter the package version:", "0.1.0")

    description = st.text_input("Enter a very brief project description:", "A simple Python project")

    st.write("By default, we have used the MIT license in the `pyproject.toml` file; you can change this by swapping to one of the other common licenses [here](https://pypi.org/classifiers/) or by instead including a license file in your repository.")

with tab1:

    folder_structure = f"""
    {repo_name}/                This is the directory you are working in now!
    ├── src/  
    │   └── {project_name}/     
    │       ├── __init__.py      Makes the folder a package.
    │       └── source.py        An example module containing source code.
    ├── tests/
    |   ├── __init__.py          Sets up the test suite.
    │   └── test_source.py       A file containing tests for the code in source.py.
    └── README.md                README with information about the project.

    """
    st.write(f"If `{repo_name}` is the root directory of your project, you might want a project structure that looks something like this:")

    st.code(folder_structure, language='text')

    st.write(f'To recreate the structure above, `cd` into your project directory (`{repo_name}`) and run the following commands (by copying and pasting the block below into the terminal):')

    # str_chunk = f"""
    # mkdir tests
    # mkdir src
    # touch pyproject.toml
    # touch README.md
    # cd src
    # mkdir {project_name}
    # cd {project_name}
    # touch __init__.py
    # touch source.py
    # cd ../.. 
    # """

    str_chunk = f"""
mkdir tests
touch tests/__init__.py
echo -e 'import sys\nsys.path.append("src")' > tests/__init__.py
mkdir src/
mkdir src/{project_name}/
touch src/{project_name}/pyproject.toml
touch src/{project_name}/README.md
touch src/{project_name}/__init__.py
touch src/{project_name}/source.py
"""

    st.code(str_chunk, language='bash')


with tab2:
    
    st.write("The previous step created a file and folder layout for your project. Open up the new `pyproject.toml` file and paste the following code template into it:")

    toml_snippet = f"""
    [build-system]
    requires = ["setuptools>=61.0", "setuptools-scm"]
    build-backend = "setuptools.build_meta"

    [project]
    name = "{project_name}"
    description = "{description}"
    version = "0.0.1"
    readme = "README.md"
    authors = [
    {{ name="{author_name}", email="{author_email}" }},
    ]
    requires-python = ">=3.10"
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    dependencies = [
        "numpy>=1.21.2",
    ]

    [project.optional-dependencies]
    test = [
        "pytest==6.2.5",
    ]
    """

    st.code(toml_snippet, language='toml')

    st.write("This file contains metadata about your project, such as the name, version, and author. It also specifies the required Python version and any dependencies your project may have. You might need to add to this, or change/add dependencies. We have added a specific version of `numpy` and `pytest` to demonstrate the syntax. You can find more information about the `pyproject.toml` file [here](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html).")

with tab3:
    st.write("[Mkdocs](https://www.mkdocs.org/) is a simple and quick documentation building library that works well with GitHub and GitHub pages.")

    st.write("From the project folder (which holds you `pyproject.toml` file), from an environment with `mkdocs` and the required extra libraries installed",
    "(see the suggested env yml at the bottom of the page to install `mkdocs` and the required extensions), you can quickly set up your docs:")
    st.code("mkdocs new .", language="bash")
    st.write("This will both create a `docs/` folder, and a `mkdocs.yml` file. Add the following to the `mkdocs.yml` file:")

    mkdocs_snippet = f"""
    site_name: {project_name} Documentation

theme:
  name: "material"

plugins:
- mkdocstrings:
    handlers:
      python:
        paths: [src]  # search packages in the src folder

nav:
  - Index: index.md
    """
    st.code(mkdocs_snippet, language='yaml')
    st.write("Then, within the `docs/` folder, you can edit the file `index.md` (or add additional markdown files), and add the following snippets:")

    st.code(f"::: {project_name}")

    st.write(f"This will include any documentation you have added to the `__init__.py` file in your `src/{project_name}/` folder.")

    st.write("You can include your API reference by including the following snippet (updating `source` with whatever your python file in your package is called):")

    st.code(f"::: {project_name}.source")

    st.write("To preview your documentation, just run `TZ=UTC mkdocs serve` from the directory that contains the `mkdocs.yml`.",
    "The `TZ=UTC` command is due to a timezone bug that causes the build to fail if not included.",
    "When happy with your documentation, you can run `TZ=UTC mkdocs build` to create a folder of webpages, then `TZ=UTC mkdocs gh-deploy`",
    "to publish these docs to GitHub. Note that you will have to enable GitHub pages, and provide actions with write permissions on your repository.",
    "For more information, see [the wiki post here](https://github.com/murphyqm/python-project-template/wiki/mkdocs-workfow).")


    st.subheader("Mkdocs env")
    st.write("You can use the following env yml to install the required `mkdocs` packages to build the docs example above.")

    mkdocs_package = """
    name: mkdocs-env
channels:
  - defaults
dependencies:
  - python=3.12
  - pip
  - pip:
    - mkdocs
    - "mkdocstrings[python]"
    - mkdocs-material
    """

    st.code(mkdocs_package, language="yaml")



with st.sidebar:

    st.header("About")
    st.write("This webapp was developed by [murphyqm](https://github.com/murphyqm) as part of the course materials for the",
    "[*SWD3: Software development in Python*](https://arc.leeds.ac.uk/training/courses/swd3/) course run by the [Research Computing Team](https://arc.leeds.ac.uk/about/team/) at the University of Leeds.")
    st.write("Find out more about [Research Computing](https://arc.leeds.ac.uk/) at Leeds.")
    st.write("You can also get in contact with me directly by leaving a message [here](https://murphyqm.github.io/murphyqm/).")