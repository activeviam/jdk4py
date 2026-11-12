"""Run a tool of the bundled JDK."""

import os
import sys
from argparse import REMAINDER, ArgumentParser
from subprocess import run

from jdk4py import JAVA_HOME


def main() -> None:
    tools = {
        path.stem: path
        for path in (JAVA_HOME / "bin").iterdir()
        if path.suffix in {"", ".exe"}
    }
    parser = ArgumentParser(prog="jdk4py", description=__doc__)
    parser.add_argument("tool", choices=sorted(tools))
    parser.add_argument("args", nargs=REMAINDER, help="arguments passed to the tool")
    arguments = parser.parse_args()
    tool = tools[arguments.tool]
    argv = [tool, *arguments.args]

    if sys.platform == "win32":
        # Windows cannot replace a process: `os.execv` starts a new one and exits right away, so the caller would lose the tool's exit code.
        sys.exit(run(argv, check=False).returncode)  # noqa: S603

    # Replace this process with the tool so that the tool receives signals and returns its exit code directly.
    os.execv(tool, argv)  # noqa: S606


if __name__ == "__main__":
    main()
