"""Setup"""

import glob
import setuptools

from distutils.dir_util import copy_tree
from os import path, walk
from pathlib import Path

with open("README.md", "r") as fh:
    long_description = fh.read()

file_directory = path.abspath(path.dirname(__file__))

def get_package_version():
    """Read the version of the package.
    See https://packaging.python.org/guides/single-sourcing-package-version
    """
    version_exports = {}
    with open(path.join(file_directory, "atotijdk", "version.py")) as file:
        exec(file.read(), version_exports)  # pylint: disable=exec-used
    return version_exports["VERSION"]

def get_java_files():
    return [
        str(Path(f).relative_to("atotijdk"))
        for f in glob.glob(
            path.join("atotijdk", "java-runtime", "**"),
            recursive=True
        )
    ]

setuptools.setup(
    name="atoti-jdk",
    version = get_package_version(),
    author="ActiveViam",
    author_email = 'dev@atoti.io',
    description = 'Packaged JDK for atoti',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atoti/atoti-jdk",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={"atotijdk": get_java_files()},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords = ['atoti', 'jdk', 'java', 'jvm'], 
    python_requires='>=3.7',
)
