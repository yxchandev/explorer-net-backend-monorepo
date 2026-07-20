from setuptools import find_packages, setup

setup(
    package_dir={"apps.consumer.src": "src"},
    packages=[
        "apps.consumer.src",
        *("apps.consumer.src." + pkg for pkg in find_packages("src")),
    ],
)
