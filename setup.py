# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata",
    version="1.0",
    author="Kenneth Thomas Barrett",
    author_email="KennethTBarrett@criptext.com",
    description="Lambdata package for LS DS 12 Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/KennethTBarrett/lambdata",
    packages=find_packages() 
)