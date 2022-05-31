import os
import platform
from typing import Mapping

from jdk4py import JAVA_VERSION

_BUILD_VERSION = 0


_AARCH64 = "aarch64"
_X64 = "x64"


# Platforms taken from https://pypi.org/project/torch/1.11.0/#files and https://anaconda.org/conda-forge/numpy/files?version=1.22.4.
_SYSTEM_TO_ARCHITECTURE_TO_PACKAGE_TYPE_TO_PLATFORM = {
    "Darwin": {
        _AARCH64: {
            "conda": "osx-arm64",
            "wheel": "macosx_11_0_arm64",
        },
        _X64: {
            "conda": "osx-64",
            "wheel": "macosx_10_9_x86_64",
        },
    },
    "Linux": {
        _AARCH64: {
            "conda": "linux-aarch64",
            "wheel": "manylinux2014_aarch64",
        },
        _X64: {
            "conda": "linux-64",
            "wheel": "manylinux1_x86_64",
        },
    },
    "Windows": {
        _X64: {
            "conda": "win-64",
            "wheel": "win_amd64",
        },
    },
}

_MACHINE_TO_ARCHITECTURE = {
    "AMD64": _X64,
    "arm64": _AARCH64,
    "x86_64": _X64,
    **{architecture: architecture for architecture in [_AARCH64, _X64]},
}


def set_env_variables_in_github_job(variables: Mapping[str, str]) -> None:
    # See https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-commands-for-github-actions#setting-an-environment-variable.
    with open(os.environ["GITHUB_ENV"], "a") as environment_file:
        for name, value in variables.items():
            environment_file.write(f"{name}={value}\n")


if __name__ == "__main__":
    architecture = os.environ.get(
        "JDK4PY_ARCHITECTURE", _MACHINE_TO_ARCHITECTURE[platform.machine()]
    )
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
