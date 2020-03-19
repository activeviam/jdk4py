"""JDK packaged for Python."""

from typing import Union, List, Optional, Any
from pathlib import Path
from subprocess import Popen

from .version import VERSION as __version__

_PARENT = Path(__file__).parent

JAVA_HOME = _PARENT.absolute() /  "java-runtime"
JAVA = JAVA_HOME  / "bin" / "java"

with open(_PARENT / "java_version") as f:
    JAVA_VERSION = f.read()

def java(
    java_args: List[str],
    **popen_args: Any,
) -> Popen:
    """Run a java process with the given arguments.

    Args:
        jvm_args: The java arguments, for instance ["HelloWorls.class", "-Xmx16G"]
        popen_args: Additional arguments to pass to the Popen

    Returns:
        The Popen process
    """
    return Popen([JAVA, *java_args], **popen_args)



def execute_jar(
    jar_path: Union[Path, str],
    jvm_args: Optional[List[str]] = None,
    **popen_args: Any,
) -> Popen:
    """Execute a JAR file.

    Args:
        jar_path: The path to the jar
        jvm_args: The JVM arguments, for instance ["-Xmx16G", "-Xms2G"]
        popen_args: Additional arguments to pass to the Popen

    Returns:
        The Popen process
    """
    if jvm_args is None:
        jvm_args = []
    return java(["-jar", str(jar_path), *jvm_args], **popen_args)

