# Atoti JDK

This is a packaged JDK for Atoti.

[![PyPI version](https://badge.fury.io/py/atoti-jdk.svg)](https://badge.fury.io/py/atoti-jdk)  


## Use the library

```bash
pip install atoti-jdk
```

Launch a JAR

```python
from atotijdk import java
java("myJar.jar")
```

Some JVM arguments can be provided, any additional argument will be passed to Popen:

```python
java_run("myJar.jar", jvm_args=["-xmx=16G"], stdout=PIPE, stderr=PIPE)
```
