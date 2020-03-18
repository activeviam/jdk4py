# Jdk4py

This is a packaged JDK for Python.

[![PyPI version](https://badge.fury.io/py/jdk4py.svg)](https://badge.fury.io/py/jdk4py)  


## Use the library

```bash
pip install jdk4py
```

Launch a JAR

```python
from jdk4py import java_jar
java_jar("myJar.jar")
```

Some JVM arguments can be provided, any additional argument will be passed to Popen:

```python
java_jar("myJar.jar", jvm_args=["-xmx=16G"], stdout=PIPE, stderr=PIPE)
```
