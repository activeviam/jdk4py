"""JDK package for Atoti."""

from typing import Union, List, Optional, Any
from pathlib import Path
from subprocess import Popen

from .version import VERSION as __version__

ATOTI_JAVA_HOME = Path(__file__).parent.absolute() /  "java-runtime"
ATOTI_JAVA = ATOTI_JAVA_HOME  / "bin" / "java"

def java_run(
    jar_path: Union[Path, str],
    jvm_args: Optional[List[str]] = None,
    **popen_args: Any,
) -> Popen:
    """Run a java jar with given arguments.

    Args:
        jar_path: The path to the jar
        jvm_args: The JVM arguments
        popen_args: Additional arguments to pass to the Popen
    """
    if jvm_args is None:
        jvm_args = []
    return Popen(
        [ATOTI_JAVA, "-jar", jar_path, *jvm_args], **popen_args
    )
