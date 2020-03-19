# Jdk4py

A packaged JDK for Python.

[![PyPI version](https://badge.fury.io/py/jdk4py.svg)](https://badge.fury.io/py/jdk4py)  

## Install

Java is made easy to install as a single pip library:

```bash
pip install jdk4py
```

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

### Java home and executable

The path to the packaged Java home folder and to java executable are also accessible:

```python
from jdk4py import JAVA, JAVA_HOME
```

The Java version can be checked with

```python
>>> from jdk4py import JAVA_VERSION
>>> JAVA_VERSION
'11.0.2'
```
