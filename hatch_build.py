import json
import platform
from pathlib import Path
from typing import Literal

from hatchling.builders.config import BuilderConfigBound
from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from hatchling.metadata.plugin.interface import MetadataHookInterface

_PROJECT_DIRECTORY = Path(__file__).parent


_Architecture = Literal["arm64", "x64"]


def _get_architecture(machine: str) -> _Architecture:
    match machine.lower():
        case "amd64" | "x64" | "x86_64":
            return "x64"
        case "aarch64" | "arm64":
            return "arm64"
        case _:
            raise ValueError(f"Unsupported machine: `{machine}`.")


def _get_platform_tag(system: str, architecture: _Architecture) -> str: # ty: ignore[invalid-return-type] incorrect `Function can implicitly return None`.
    # Tag values taken from https://pypi.org/project/numpy/2.1.0/#files.
    match system.lower():
        case "darwin":
            match architecture:
                case "arm64":
                    return "macosx_11_0_arm64"
                case "x64":
                    return "macosx_10_9_x86_64"
        case "linux":
            match architecture:
                case "arm64":
                    return "manylinux_2_17_aarch64"
                case "x64":
                    return "manylinux_2_17_x86_64"
        case "windows":
            match architecture:
                case "x64":
                    return "win_amd64"
                case _:
                    raise ValueError(
                        f"Unsupported {system} architecture: `{architecture}`.",
                    )
        case _:
            raise ValueError(f"Unsupported system: `{system}`.")


class BuildHook(BuildHookInterface[BuilderConfigBound]):
    def initialize(
        self,
        version: str,  # noqa: ARG002
        build_data: dict[str, object],
    ) -> None:
        python_tag = "py3"
        abi_tag = "none"

        system = platform.system()
        architecture = _get_architecture(platform.machine())
        platform_tag = _get_platform_tag(system, architecture)

        build_data["tag"] = f"{python_tag}-{abi_tag}-{platform_tag}"


class MetadataHook(MetadataHookInterface):
    def update(self, metadata: dict[str, object]) -> None:
        version = json.loads(
            (_PROJECT_DIRECTORY / "src" / "jdk4py" / "version.json").read_bytes(),
        )
        assert isinstance(version, str)
        metadata["version"] = version
