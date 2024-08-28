import os
import platform
from typing import Literal, Mapping

from jdk4py import JAVA_VERSION

_Architecture = Literal["aarch64", "x64"]
_PackageType = Literal["conda", "wheel"]

_MACHINE_TO_ARCHITECTURE: Mapping[str, _Architecture] = {
    "AMD64": "x64",
    "arm64": "aarch64",
    "x64": "x64",
    "x86_64": "x64",
}

# Platforms taken from https://anaconda.org/conda-forge/numpy/files?version=2.1.0 and https://pypi.org/project/numpy/2.1.0/#files
_SYSTEM_TO_ARCHITECTURE_TO_PACKAGE_TYPE_TO_PLATFORM: Mapping[
    str, Mapping[_Architecture, Mapping[_PackageType, str]]
] = {
    "Darwin": {
        "aarch64": {
            "conda": "osx-arm64",
            "wheel": "macosx_14_0_arm64",
        },
        "x64": {
            "conda": "osx-64",
            "wheel": "macosx_13_0_x86_64",
        },
    },
    "Linux": {
        "aarch64": {
            "conda": "linux-aarch64",
            "wheel": "manylinux_2_17_aarch64",
        },
        "x64": {
            "conda": "linux-64",
            "wheel": "manylinux_2_17_x86_64",
        },
    },
    "Windows": {
        "x64": {
            "conda": "win-64",
            "wheel": "win_amd64",
        },
    },
}


def set_env_variables_in_github_job(variables: Mapping[str, str]) -> None:
    # See https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-commands-for-github-actions#setting-an-environment-variable.
    with open(os.environ["GITHUB_ENV"], "a") as environment_file:
        for name, value in variables.items():
            environment_file.write(f"{name}={value}\n")


if __name__ == "__main__":
    architecture = _MACHINE_TO_ARCHITECTURE[platform.machine()]
    system = platform.system()

    set_env_variables_in_github_job(
        {
            "JDK4PY_CONDA_PLATFORM": _SYSTEM_TO_ARCHITECTURE_TO_PACKAGE_TYPE_TO_PLATFORM[
                system
            ][architecture]["conda"],
            "JDK4PY_JAVA_VERSION": ".".join(str(number) for number in JAVA_VERSION),
            "JDK4PY_WHEEL_PLATFORM": _SYSTEM_TO_ARCHITECTURE_TO_PACKAGE_TYPE_TO_PLATFORM[
                system
            ][architecture]["wheel"],
        }
    )
