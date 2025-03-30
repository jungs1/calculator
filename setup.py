from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    description="A simple calculator library",
    author="Example Author",
    author_email="author@example.com",
    package_dir={"": "calculator"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
