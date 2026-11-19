# jdk4py

[![PyPI](https://img.shields.io/pypi/v/jdk4py?style=flat-square)](https://pypi.org/project/jdk4py)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Factiveviam%2Fjdk4py%2Fmain%2Fpyproject.toml&style=flat-square)](https://github.com/activeviam/jdk4py/blob/main/pyproject.toml)
[![License](https://img.shields.io/badge/license-GPL--2.0%20with%20Classpath%20exception-blue?style=flat-square)](https://github.com/activeviam/jdk4py/blob/main/LICENSE)

A JDK shipped in a Python package.

## Install

```bash
pip install jdk4py
```

or

```bash
uv add jdk4py
```

## Usage

### Command line

The `jdk4py` command runs a tool of the bundled JDK, such as `java`, `keytool`, or `jcmd`.
With [uvx](https://docs.astral.sh/uv/guides/tools/), it runs without installing jdk4py first:

```bash
uvx jdk4py java -version
```

### Python API

```python
>>> from jdk4py import JAVA, JAVA_FULL_VERSION, JAVA_HOME, JAVA_VERSION
>>> JAVA_HOME
PosixPath('/Users/johndoe/dev/jdk4py/jdk4py/java-runtime')
>>> JAVA
PosixPath('/Users/johndoe/dev/jdk4py/jdk4py/java-runtime/bin/java')
>>> JAVA_VERSION
(25, 0, 5)
>>> JAVA_FULL_VERSION
'25.0.5.1+2'
>>> from subprocess import run
>>> some_java_options = ["-Xmx16G", "-Xms2G"]
>>> run(
...     [JAVA, *some_java_options, "-jar", "HelloWorld.jar"],
...     capture_output=True,
...     check=True,
...     text=True,
... ).stdout.strip()
'Hello, World'
```

## Versioning

`jdk4py`'s version contains 4 numbers:

- The first 3 numbers are the version line of the bundled JDK, such as 25.0.5. `JAVA_VERSION` holds them.
- The fourth number counts the releases of jdk4py in that line. A new release can bundle another build of the JDK, such as an OpenJDK patch release, or change the library.

The fourth number is not part of the JDK version, even when they look alike.
`JAVA_FULL_VERSION` holds the exact version of the bundled JDK with its build number, such as 25.0.5.1+2: the version can have more than 3 numbers.

| jdk4py   | JDK        |
| -------- | ---------- |
| 25.0.5.1 | 25.0.5.1+2 |
| 25.0.5.0 | 25.0.5+8   |
| 25.0.2.1 | 25.0.2+10  |
| 25.0.2.0 | 25.0.2+10  |
