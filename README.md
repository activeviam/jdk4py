# jdk4py

A JDK shipped in a Python package.

[![PyPI version](https://badge.fury.io/py/jdk4py.svg)](https://badge.fury.io/py/jdk4py)

## Install

```bash
pip install jdk4py
```

## Usage

```python
>>> from jdk4py import JAVA, JAVA_FULL_VERSION, JAVA_HOME, JAVA_VERSION
>>> JAVA_HOME
PosixPath('/Users/johndoe/dev/jdk4py/jdk4py/java-runtime')
>>> JAVA
PosixPath('/Users/johndoe/dev/jdk4py/jdk4py/java-runtime/bin/java')
>>> JAVA_VERSION
(21, 0, 8)
>>> JAVA_FULL_VERSION
'21.0.8+9'
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

- The first 3 numbers are the version line of the bundled JDK, such as 21.0.8. `JAVA_VERSION` holds them.
- The fourth number counts the releases of jdk4py in that line. A new release can bundle another build of the JDK, such as an OpenJDK patch release, or change the library.

The fourth number is not part of the JDK version, even when they look alike.
`JAVA_FULL_VERSION` holds the exact version of the bundled JDK with its build number, such as 21.0.13.1+2: the version can have more than 3 numbers.

| jdk4py   | JDK      |
| -------- | -------- |
| 21.0.8.2 | 21.0.8+9 |
| 21.0.8.1 | 21.0.8+9 |
| 21.0.8.0 | 21.0.8+9 |
