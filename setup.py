import glob
import setuptools
import sys

from os import path, environ
from pathlib import Path

_NAME = "jdk4py"

_JAVA_FILES = [
    str(Path(f).relative_to(_NAME))
    for f in glob.glob(path.join(_NAME, "java-runtime", "**"), recursive=True)
]

_PROJECT_DIR = Path(__file__).parent

_JAVA_VERSION_FILENAME = "java_version.txt"
_LIB_VERSION_FILENAME = "lib_version.txt"

_VERSION = ".".join(
    [
        (_PROJECT_DIR / _NAME / filename).read_text().strip()
        for filename in (_JAVA_VERSION_FILENAME, _LIB_VERSION_FILENAME)
    ]
)

_PLATFORMS = {
    "macos-latest": "macosx_10_9_x86_64",
    "ubuntu-latest": "manylinux1_x86_64",
    "windows-latest": "win_amd64",
}

if "--plat-name" not in sys.argv and "PLATFORM" in environ:
    machine = environ["PLATFORM"]
    platform = _PLATFORMS[machine]
    sys.argv.append("--plat-name")
    sys.argv.append(platform)

setuptools.setup(
    name=_NAME,
    version=_VERSION,
    author="atoti",
    author_email="dev@atoti.io",
    description="Packaged JDK for Python",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/atoti/jdk4py",
    packages=setuptools.find_packages(exclude=["tests"]),
    package_data={_NAME: [*_JAVA_FILES, _JAVA_VERSION_FILENAME, _LIB_VERSION_FILENAME]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords=["jdk", "java", "jvm", "jre"],
    python_requires=">=3.6",
)
