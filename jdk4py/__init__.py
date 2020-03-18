"""JDK packaged for Python."""

from typing import Union, List, Optional, Any
from pathlib import Path
from subprocess import Popen

from .version import VERSION as __version__

PACKAGED_JAVA_HOME = Path(__file__).parent.absolute() /  "java-runtime"
PACKAGED_JAVA = PACKAGED_JAVA_HOME  / "bin" / "java"

def java_jar(
    jar_path: Union[Path, str],
    jvm_args: Optional[List[str]] = None,
    **popen_args: Any,
) -> Popen:
    """Execute a JAR file.

    Args:
        jar_path: The path to the jar
        jvm_args: The JVM arguments
        popen_args: Additional arguments to pass to the Popen
    """
    if jvm_args is None:
        jvm_args = []
    return Popen(
        [PACKAGED_JAVA, "-jar", jar_path, *jvm_args], **popen_args
    )
