JARs in this folder can be generated like this:

```bash
cd ..
javac resources/$CLASS_NAME.java
jar cfe resources/$CLASS_NAME.jar resources.$CLASS_NAME resources/$CLASS_NAME.class
rm resources/$CLASS_NAME.class
jar tf resources/$CLASS_NAME.jar
```
