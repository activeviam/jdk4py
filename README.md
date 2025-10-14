# jdk4py

A JDK shipped in a Python package.

[![PyPI version](https://badge.fury.io/py/jdk4py.svg)](https://badge.fury.io/py/jdk4py)

## Install

```bash
pip install jdk4py
```

or as a Conda package:

```bash
conda config --add channels https://conda.atoti.io
conda install jdk4py
```

## Usage

```python
>>> from jdk4py import JAVA, JAVA_HOME, JAVA_VERSION
>>> JAVA_HOME
PosixPath('/Users/johndoe/dev/jdk4py/jdk4py/java-runtime')
>>> JAVA
PosixPath('/Users/johndoe/dev/jdk4py/jdk4py/java-runtime/bin/java')
>>> JAVA_VERSION
(21, 0, 8)
>>> from subprocess import run
>>> some_java_options = ["-Xmx16G", "-Xms2G"]
>>> run(
...     [JAVA, "-jar", "HelloWorld.jar", *some_java_options],
...     capture_output=True,
...     check=True,
...     text=True,
... ).stdout.strip()
"Hello, World!"
```

## Versioning

`jdk4py`'s version contains 4 numbers:

- The first 3 numbers correspond to the JDK version.
- The fourth number is the library API version.
