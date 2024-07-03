import streamlit as st

st.title('Basic Python Project Structure')

st.write("This webapp creates customised code snippets to help you set up a Python package project.",
"First, look through the **Picking a project name** tab and decide on a name for your Python package.",
"Then, go to the **Project details** tab and fill in information for your project.",
"Then, you can generate a sensible project folder structure using the `bash` scripts in the tab **Folder Structure**.",
"You can build your Python package using the generated `pyproject.toml` template in the **pyproject.toml** tab." )

tablist = ["Picking a project name", "Project details", "Folder structure", "pyproject.toml"]

intro, tab0, tab1, tab2 = st.tabs(tablist)

with intro:
    st.write("Basic information on picking a project name.")

with tab0:
    project_name = st.text_input("Enter your package name (letters, number and underscores only!):", "example_package")

    author_name = st.text_input("Enter the author's full name:", "Author Full Name")

    author_email = st.text_input("Enter the author's email:", "authors_email@goes_here.ie")

    version = st.text_input("Enter the package version:", "0.1.0")

    description = st.text_input("Enter a very brief project description:", "A simple Python project")

    st.write("By default, we have used the MIT license in the `pyproject.toml` file; you can change this by swapping to one of the other common licenses [here](https://pypi.org/classifiers/) or by instead including a license file in your repository.")

with tab1:

    folder_structure = f"""
    your_git_repo/              This is the directory you are working in now!
    ├── src/  
    │   └── {project_name}/     
    │       ├── __init__.py      Makes the folder a package.
    │       └── source.py        An example module containing source code.
    ├── tests/  
    │   └── test_source.py       A file containing tests for the code in source.py.
    └── README.md                README with information about the project.

    """
    st.write("If `your_git_repo` is the root directory of your project, you might want a project structure that looks something like this:")

    st.code(folder_structure, language='text')

    st.write('To recreate the structure above, `cd` into your project directory and run the following commands (by copying and pasting the block below into the terminal):')

    str_chunk = f"""
    mkdir tests
    mkdir src
    touch pyproject.toml
    touch README.md
    cd src
    mkdir {project_name}
    cd {project_name}
    touch __init__.py
    touch source.py
    cd ../.. 
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
