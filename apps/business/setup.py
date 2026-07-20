from setuptools import find_packages, setup

setup(
    package_dir={"apps.business.src": "src"},
    packages=[
        "apps.business.src",
        *("apps.business.src." + pkg for pkg in find_packages("src")),
    ],
)
