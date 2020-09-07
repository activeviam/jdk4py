from pathlib import Path

_PROJECT_DIRECTORY = Path(__file__).parent.parent
_JDK4PY_DIRECTORY = _PROJECT_DIRECTORY / "jdk4py"
_JAVA_VERSION_FILENAME = "java_version.txt"
_LIB_VERSION_FILENAME = "lib_version.txt"


def set_java_version_env_variable_in_github_job():
    java_version = (_JDK4PY_DIRECTORY / _JAVA_VERSION_FILENAME).read_text().strip()
    # See https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions#setting-an-environment-variable.
    print(f"::set-env name=JAVA_VERSION::{java_version}")


def set_jdk4py_version_env_variable_in_github_job():
    version = ".".join(
        [
            (_JDK4PY_DIRECTORY / filename).read_text().strip()
            for filename in (_JAVA_VERSION_FILENAME, _LIB_VERSION_FILENAME)
        ]
    )
    print(f"::set-env name=JDK4PY_VERSION::{version}")

if __name__ == "__main__":
    set_java_version_env_variable_in_github_job()
    set_jdk4py_version_env_variable_in_github_job()