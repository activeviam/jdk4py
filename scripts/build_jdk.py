"""Script to build the Java executables files."""

from subprocess import Popen, PIPE
from pathlib import Path
from shutil import rmtree


PROJECT_FOLDER = Path(__file__).parent.parent
JAVA_PATH = PROJECT_FOLDER / "jdk4py" / "java-runtime"


def main():
    rmtree(JAVA_PATH, ignore_errors=True)
    process = Popen(
        [
            "jlink",
            "--no-header-files",
            "--no-man-pages",
            "--compress=2",
            "--strip-debug",
            "--add-modules",
            "java.se,jdk.unsupported,jdk.security.auth",
            "--output",
            str(JAVA_PATH)
        ],
        stdout=PIPE,
        stderr=PIPE)
    out, err = process.communicate()
    if (process.returncode == 0):
        print("Successfully built the Java executables.")
        return
    else:
        print(f"Failed to build the Java executables with error code {process.returncode}.")
        print(out)
        raise SystemError(err)

if __name__ == "__main__":
    main()

    