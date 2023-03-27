import setuptools

PACKAGE_NAME = "windowsget_pdm"
COMMAND_NAME = "windowsget_pdm"

setuptools.setup(
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        "console_scripts": [
            f"{COMMAND_NAME} = {PACKAGE_NAME}.cli:main",
        ]
    }
)
