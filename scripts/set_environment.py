import os
import platform
from typing import Literal, Mapping

from jdk4py import JAVA_VERSION


_BUILD_VERSION = 0


_Architecture = Literal["aarch64", "x64"]
_PackageType = Literal["conda", "wheel"]

_MACHINE_TO_ARCHITECTURE: Mapping[str, _Architecture] = {
    "aarch64": "aarch64",
    "AMD64": "x64",
    "arm64": "aarch64",
    "x64": "x64",
    "x86_64": "x64",
}

# Platforms taken from https://pypi.org/project/torch/1.11.0/#files and https://anaconda.org/conda-forge/numpy/files?version=1.22.4.
_SYSTEM_TO_ARCHITECTURE_TO_PACKAGE_TYPE_TO_PLATFORM: Mapping[
    str, Mapping[_Architecture, Mapping[_PackageType, str]]
] = {
    "Darwin": {
        "aarch64": {
            "conda": "osx-arm64",
            "wheel": "macosx_11_0_arm64",
        },
        "x64": {
            "conda": "osx-64",
            "wheel": "macosx_10_9_x86_64",
        },
    },
    "Linux": {
        "aarch64": {
            "conda": "linux-aarch64",
            "wheel": "manylinux2014_aarch64",
        },
        "x64": {
            "conda": "linux-64",
            "wheel": "manylinux1_x86_64",
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
            "JDK4PY_BUILD_NUMBER": str(_BUILD_VERSION),
            "JDK4PY_CONDA_PLATFORM": _SYSTEM_TO_ARCHITECTURE_TO_PACKAGE_TYPE_TO_PLATFORM[
                system
            ][
                architecture
            ][
                "conda"
            ],
            "JDK4PY_JAVA_VERSION": ".".join(str(number) for number in JAVA_VERSION),
            "JDK4PY_WHEEL_PLATFORM": _SYSTEM_TO_ARCHITECTURE_TO_PACKAGE_TYPE_TO_PLATFORM[
                system
            ][
                architecture
            ][
                "wheel"
            ],
        }
    )
