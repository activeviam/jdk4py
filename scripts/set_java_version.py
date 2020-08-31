from pathlib import Path

_PROJECT_DIRECTORY = Path(__file__).parent.parent
_JAVA_VERSION_FILEPATH = _PROJECT_DIRECTORY / "jdk4py" / "java_version.txt"


def set_java_version_env_variable_in_github_job():
    java_version = _JAVA_VERSION_FILEPATH.read_text().strip()
    # See https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions#setting-an-environment-variable.
    print(f"::set-env name=JAVA_VERSION::{java_version}")


if __name__ == "__main__":
    set_java_version_env_variable_in_github_job()
