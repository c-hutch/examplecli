from setuptools import setup

setup(
    name="examplecli",
    version="0.1",
    description="Basic containerized cli file",
    url="http://github.com/c-hutch/examplecli",
    author="C Hutcherson",
    author_email="chutch9000@yahoo.com",
    license="MIT",
    packages=["examplecli"],
    install_requires=["pyyaml"],
    zip_safe=True,
)
