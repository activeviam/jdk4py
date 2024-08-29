from jdk4py import JAVA_VERSION

if __name__ == "__main__":
    print(  # noqa: T201
        f'java-version="{".".join(str(number) for number in JAVA_VERSION)}"',
    )
