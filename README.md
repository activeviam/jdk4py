# Jdk4py

A packaged JDK for Python.

[![PyPI version](https://badge.fury.io/py/jdk4py.svg)](https://badge.fury.io/py/jdk4py)

## Install

Java is made easy to install as a single pip library:

```bash
pip install jdk4py
```

or as a Conda package:

```bash
conda config --add channels https://conda.atoti.io
conda install jdk4py
```

## Versioning

jdk4py version contains 4 figures:

  - The first 3 figures are the Java version
  - The fourth is jdk4py specific: it starts at 0 for each Java version and then increases.

## API

### Execute a JAR

```python
from jdk4py import execute_jar
execute_jar("myJar.jar")
```

Some JVM arguments can be provided, any additional argument will be passed to Popen:

```python
execute_jar("myJar.jar", jvm_args=["-xmx=16G"], stdout=PIPE, stderr=PIPE)
```

### Home and executable paths

The paths to the packaged Java home directory and to the Java executable are also accessible:

```python
from jdk4py import JAVA, JAVA_HOME
```

The Java version can be checked with:

```python
>>> from jdk4py import JAVA_VERSION
>>> JAVA_VERSION
'11.0.2'
```
