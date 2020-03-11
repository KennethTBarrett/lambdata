import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-KennethTBarrett", 
    version="0.0.1",
    author="Kenneth Thomas Barrett",
    author_email="KennethTBarrett@criptext.com",
    description="Lambda School DS12 Unit 3 Sprint 1 Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)