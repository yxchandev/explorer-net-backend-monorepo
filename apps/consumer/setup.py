from setuptools import find_packages, setup

setup(
    package_dir={"consumer": "src"},
    packages=["consumer", *("consumer." + pkg for pkg in find_packages("src"))],
)
