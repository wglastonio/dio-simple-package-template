from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="Wglastonio",
    author_email="wglastonio@gmail.com",
    description="Example of package creation",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wglastonio/dio-simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='3.13 and above',
)