"""Setup"""

import glob
import setuptools
import sys

from os import path, environ
from pathlib import Path

_NAME = "jdk4py"
_PROJECT_DIR = Path(__file__).parent


with open("README.md", "r") as fh:
    long_description = fh.read()

file_directory = path.abspath(path.dirname(__file__))

def get_package_version():
    """Read the version of the package.
    See https://packaging.python.org/guides/single-sourcing-package-version
    """
    with open(_PROJECT_DIR / _NAME / "java_version") as f:
        java_version = f.read()

    with open(_PROJECT_DIR / _NAME / "version") as f:
        lib_version = f.read()
    return f"{java_version}.{lib_version}"

def get_java_files():
    return [
        str(Path(f).relative_to(_NAME))
        for f in glob.glob(
            path.join(_NAME, "java-runtime", "**"),
            recursive=True
        )
    ]

_PLATFORMS = {
    "macos-latest": "macosx_10_9_x86_64",
    "ubuntu-latest": "manylinux1_x86_64",
    "windows-latest": "win_amd64"
}

if "--plat-name" not in sys.argv and "PLATFORM" in environ:
    machine = environ["PLATFORM"]
    platform = _PLATFORMS[machine]
    sys.argv.append("--plat-name")
    sys.argv.append(platform)

setuptools.setup(
    name=_NAME,
    version = get_package_version(),
    author="ActiveViam",
    author_email = 'dev@atoti.io',
    description = 'Packaged JDK for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atoti/jdk4py",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={_NAME: [ *get_java_files(), "java_version", "version"] },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords = ['jdk', 'java', 'jvm', 'jre'], 
    python_requires='>=3.6',
)
