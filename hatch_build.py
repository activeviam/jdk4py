from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from hatchling.builders.config import BuilderConfigBound
from hatchling.metadata.plugin.interface import MetadataHookInterface


class BuildHook(BuildHookInterface[BuilderConfigBound]):
    def initialize(self, version: str, build_data: dict[str, object]) -> None:
        build_data["tag"] = "py3-none-macosx_14_0_arm64"


_LIB_VERSION = 1


class MetadataHook(MetadataHookInterface):
    def update(self, metadata: dict[str, object]) -> None:
        metadata["version"] = f"21.0.4.{_LIB_VERSION}"
