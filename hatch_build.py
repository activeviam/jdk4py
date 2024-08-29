from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from hatchling.builders.config import BuilderConfigBound
from hatchling.metadata.plugin.interface import MetadataHookInterface
from pathlib import Path
from subprocess import check_output

_PROJECT_DIRECTORY = Path(__file__).parent


class BuildHook(BuildHookInterface[BuilderConfigBound]):
    def initialize(self, version: str, build_data: dict[str, object]) -> None:
        python_tag = "py3"
        abi_tag = "none"
        platform_tag = check_output(
            [
                "python",
                str(_PROJECT_DIRECTORY / "scripts" / "get_platform_tag.py"),
                "wheel",
            ],
            text=True,
        ).strip()
        build_data["tag"] = "-".join([python_tag, abi_tag, platform_tag])


class MetadataHook(MetadataHookInterface):
    def update(self, metadata: dict[str, object]) -> None:
        java_version = (
            (_PROJECT_DIRECTORY / "src" / "jdk4py" / "java_version.txt")
            .read_text()
            .strip()
        )
        lib_version = 1
        metadata["version"] = f"{java_version}.{lib_version}"
