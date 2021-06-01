from os import environ
from pathlib import Path
from typing import Mapping

_PROJECT_DIRECTORY = Path(__file__).parent.parent
_SOURCE_DIRECTORY = _PROJECT_DIRECTORY / "jdk4py"


def set_env_variables_in_github_job(variables: Mapping[str, str]):
    # See https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-commands-for-github-actions#setting-an-environment-variable.
    with open(environ["GITHUB_ENV"], "a") as environment_file:
        for name, value in variables.items():
            environment_file.write(f"{name}={value}\n")


if __name__ == "__main__":
    build_number, java_version, lib_version = (
        (_SOURCE_DIRECTORY / filename).read_text().strip()
        for filename in ("build_number.txt", "java_version.txt", "lib_version.txt")
    )

    set_env_variables_in_github_job(
        {
            "JAVA_VERSION": java_version,
            "JDK4PY_BUILD_NUMBER": build_number,
            "JDK4PY_VERSION": ".".join((java_version, lib_version)),
        }
    )
