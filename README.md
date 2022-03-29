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
(17, 0, 2)
>>> from subprocess import check_output
>>> some_java_options = ["-Xmx16G", "-Xms2G"]
>>> check_output([str(JAVA), "-jar", "HelloWorld.jar",  *some_java_options])
b"Hello, World!"
```

## Versioning

`jdk4py` version contains 4 figures:

- The first 3 figures are the Java version.
- The fourth is `jdk4py` specific: it starts at 0 for each Java version and then increases.
