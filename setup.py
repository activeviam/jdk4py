import os
from pathlib import Path
from sys import argv

from setuptools import find_packages, setup

_LIB_VERSION = 0

_NAME = "jdk4py"
_PROJECT_DIRECTORY = Path(__file__).parent

_SOURCE_DIRECTORY = _PROJECT_DIRECTORY / _NAME

_JAVA_RUNTIME_FOLDER = "java-runtime"

_JAVA_FILES = [_JAVA_RUNTIME_FOLDER] + [
    str(path.relative_to(_SOURCE_DIRECTORY))
    for path in (_SOURCE_DIRECTORY / _JAVA_RUNTIME_FOLDER).rglob("*")
]

_JAVA_VERSION_FILENAME = "java_version.txt"

_VERSION = ".".join(
    (
        (_SOURCE_DIRECTORY / _JAVA_VERSION_FILENAME).read_text().strip(),
        str(_LIB_VERSION),
    )
)

_PLATFORM_NAME_ARGUMENT_NAME = "--plat-name"


def _add_platform_name_argument_when_building_python_wheel():
    platform = os.environ.get("JDK4PY_WHEEL_PLATFORM")
    if platform and "bdist_wheel" in argv and _PLATFORM_NAME_ARGUMENT_NAME not in argv:
        argv.extend([_PLATFORM_NAME_ARGUMENT_NAME, platform])


setup_args = dict(
    name=_NAME,
    version=_VERSION,
    author="atoti",
    author_email="dev@atoti.io",
    description="Packaged JDK for Python",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/atoti/jdk4py",
    packages=find_packages(exclude=["scripts", "tests"]),
    package_data={_NAME: [*_JAVA_FILES, _JAVA_VERSION_FILENAME, "py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
    keywords=["jdk", "java", "jvm", "jre"],
    python_requires=">=3.7",
)

if __name__ == "__main__":
    _add_platform_name_argument_when_building_python_wheel()
    setup(**setup_args)
