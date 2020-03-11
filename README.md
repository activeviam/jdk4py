# Atoti JDK

This is a packaged JDK for Atoti.

## Use the library

```bash
pip install atoti-jdk
```

```python
from atotijdk import java
java("myJar.jar")
```

## Build, test and deploy


### Install dependencies

```bash
pipenv install
```

When building the wheel the Specify the platform of the build must be added according to [naming convention](https://www.python.org/dev/peps/pep-0427/#file-name-convention)

### Build the JDK executable

```bash
jlink --no-header-files --no-man-pages --compress=2 --strip-debug --add-modules java.se,jdk.unsupported --output atoti-jdk/java-runtime
```

### Test

```bash
pipenv run pytest
```

### Build the wheel

```bash
pipenv run python setup.py bdist_wheel --plat-name manylinux1_x86_64
```

Other platform names:
  - win-amd64
  - macosx_10_11_x86_64

### Deploy

Set the token as envrionment variable

```bash
pipenv run twine upload dist/* --username __token__ --password $ATOTI_TOKEN
```