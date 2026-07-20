from setuptools import find_packages, setup

setup(
    package_dir={"packages.pylib.src": "src"},
    packages=[
        "packages.pylib.src",
        *("packages.pylib.src." + pkg for pkg in find_packages("src")),
    ],
)
