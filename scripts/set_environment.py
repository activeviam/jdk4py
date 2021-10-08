import os
import platform
from typing import Mapping

from jdk4py import JAVA_VERSION

_BUILD_VERSION = 0

_SYSTEM_TO_CONDA_ARCH = {
    "Darwin": "osx-64",
    "Linux": "linux-64",
    "Windows": "win-64",
}


def set_env_variables_in_github_job(variables: Mapping[str, str]):
    # See https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-commands-for-github-actions#setting-an-environment-variable.
    with open(os.environ["GITHUB_ENV"], "a") as environment_file:
        for name, value in variables.items():
            environment_file.write(f"{name}={value}\n")


if __name__ == "__main__":
    set_env_variables_in_github_job(
        {
            "JDK4PY_BUILD_NUMBER": str(_BUILD_VERSION),
            "JDK4PY_CONDA_ARCH": _SYSTEM_TO_CONDA_ARCH[platform.system()],
            "JDK4PY_JAVA_VERSION": ".".join(str(number) for number in JAVA_VERSION),
        }
    )
