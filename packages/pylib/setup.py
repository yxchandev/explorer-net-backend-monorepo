from setuptools import find_packages, setup

setup(
    package_dir={"pylib": "src"},
    packages=["pylib", *("pylib." + pkg for pkg in find_packages("src"))],
)
