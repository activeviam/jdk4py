import re
import sys
from pathlib import Path
from shutil import which
from subprocess import CompletedProcess, run

import pytest

from jdk4py import JAVA_HOME


@pytest.fixture(scope="module")
def command() -> str:
    path = which(
        "jdk4py",
        # Not from `$PATH`, which could find another installation.
        path=Path(sys.executable).parent,
    )
    assert path, "The `jdk4py` command is not installed."
    return path


def _run(command: str, /, *args: str) -> CompletedProcess[str]:
    return run(  # noqa: S603
        [command, *args],
        capture_output=True,
        check=False,
        text=True,
    )


def test_bundled_tool_execution(command: str) -> None:
    completed_process = _run(command, "java", "-XshowSettings:properties", "-version")
    output = completed_process.stderr
    assert completed_process.returncode == 0, output
    match = re.search(r"^ *java\.home = (?P<path>.+)$", output, re.MULTILINE)
    assert match, f"Unexpected output:\n{output}"
    assert Path(match.group("path")).resolve() == JAVA_HOME.resolve()


def test_exit_code_forwarding(command: str) -> None:
    completed_process = _run(command, "java", "-unknown-option")
    assert completed_process.returncode == 1, completed_process.stderr


def test_unknown_tool_rejection(command: str) -> None:
    completed_process = _run(command, "not-a-jdk-tool")
    argparse_usage_error_exit_code = 2
    assert completed_process.returncode == argparse_usage_error_exit_code
    assert "invalid choice: 'not-a-jdk-tool'" in completed_process.stderr
