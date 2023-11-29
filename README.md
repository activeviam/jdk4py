# jdk4py

A packaged JDK for Python.

[![PyPI version](https://badge.fury.io/py/jdk4py.svg)](https://badge.fury.io/py/jdk4py)

## Install

Java is made easy to install as a single Python package:

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
(17, 0, 8, 1)
>>> from subprocess import check_output
>>> some_java_options = ["-Xmx16G", "-Xms2G"]
>>> check_output([str(JAVA), "-jar", "HelloWorld.jar",  *some_java_options])
b"Hello, World!"
```

## Versioning

`jdk4py`'s version contains at least 4 numbers:

- The last number is `jdk4py` specific: it starts at 0 for each Java version and then increases.
- The other numbers are the Java version.
