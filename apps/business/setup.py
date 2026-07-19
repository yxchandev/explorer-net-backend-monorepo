from setuptools import find_packages, setup

setup(
    package_dir={"business": "src"},
    packages=["business", *("business." + pkg for pkg in find_packages("src"))],
)
