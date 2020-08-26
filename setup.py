import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="django-segno-qr",
    version="1.0.2",
    author="Ideler IT-Service GmbH",
    author_email="hosting@ideler.de",
    description="Django template tag for generating QR codes using segno",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ideler/django-segno-qr",
    packages=setuptools.find_packages(),
    install_requires=['segno', 'django'],
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django :: 3.0",
    ],
)
