from setuptools import setup

setup(
    name="examplecli",
    version="0.1",
    description="Basic containerized python cli",
    url="http://github.com/c-hutch/examplecli",
    author="C Hutcherson",
    author_email="chutch9000@yahoo.com",
    license="MIT",
    packages=["app"],
    install_requires=["pyyaml"],
    zip_safe=True,
)
