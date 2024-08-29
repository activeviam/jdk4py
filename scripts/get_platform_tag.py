import platform
from typing import Literal, Mapping, get_args, cast
from argparse import ArgumentParser


_Architecture = Literal["aarch64", "x64"]
_PackageType = Literal["conda", "wheel"]
_System = Literal["Darwin", "Linux", "Windows"]


# Tags taken from https://anaconda.org/conda-forge/numpy/files?version=2.1.0 and https://pypi.org/project/numpy/2.1.0/#files
_PLATFORM_TAG_FROM_PACKAGE_TYPE_FROM_ARCHITECTURE_FROM_SYSTEM: Mapping[
    _System, Mapping[_Architecture, Mapping[_PackageType, str]]
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


def _get_architecture(machine: str, /) -> _Architecture:
    match machine:
        case "AMD64", "x64", "x86_64":
            return "x64"
        case "arm64":
            return "aarch64"
        case _:
            raise ValueError(f"Unsupported machine: `{machine}`")


def get_platform_tag(
    system: str, architecture: _Architecture, package_type: _PackageType, /
) -> str:
    # Keep OS versions in sync with the ones in the GitHub Actions files.
    match system:
        case "Darwin":
            match architecture:
                case "aarch64":
                    match package_type:
                        case "conda":
                            return "osx-arm64"
                        case "wheel":
                            return "macosx_14_0_arm64"
                case "x64":
                    match package_type:
                        case "conda":
                            return "osx-64"
                        case "wheel":
                            return "macosx_13_0_x86_64"
        case "Linux":
            match architecture:
                case "aarch64":
                    match package_type:
                        case "conda":
                            return "linux-aarch64"
                        case "wheel":
                            return "manylinux_2_17_aarch64"
                case "x64":
                    match package_type:
                        case "conda":
                            return "linux-64"
                        case "wheel":
                            return "manylinux_2_17_x86_64"
        case "Windows":
            match architecture:
                case "x64":
                    match package_type:
                        case "conda":
                            return "win-64"
                        case "wheel":
                            return "win_amd64"
                case _:
                    raise ValueError(
                        f"Unsupported {system} architecture: `{architecture}`."
                    )
        case _:
            raise ValueError(f"Unsupported system: `{system}`.")


if __name__ == "__main__":
    system = platform.system()
    architecture = _get_architecture(platform.machine())

    parser = ArgumentParser()
    parser.add_argument("package_type", choices=get_args(_PackageType))
    args = parser.parse_args()
    package_type = cast(_PackageType, args.package_type)

    platform_tag = get_platform_tag(system, architecture, package_type)
    print(platform_tag)
