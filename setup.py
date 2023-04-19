from setuptools import (
    setup,
    find_packages,
)

setup(
    name="Poly-REaDDIT",
    version="0.0.1",
    author="Aaarghhh",
    author_email="giacomo@udontneed.it",
    packages=["poly-readdit"],
    package_dir={'':'src'},
    include_package_data=True,
    entry_points={"console_scripts": ["poly-readdit = poly-readdit.poly-readdit:run"]},
    url="https://github.com/aaarghhh/Poly-REaDDIT",
    license="MIT",
    description='"Poly REaDDIT" A tool for gathering Reddit user information and also retrieve the related Polygon (MATIC) public address.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "beautifulsoup4==4.12.2",
        "certifi==2022.12.7",
        "charset-normalizer==3.1.0",
        "idna==3.4",
        "requests==2.28.2",
        "soupsieve==2.4",
        "urllib3==1.26.15"
    ],
    zip_safe=False,
)