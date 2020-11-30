import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ATMcontroller", # Replace with your own username
    version="0.0.1",
    author="Nithish Kumar",
    author_email="nithish@terpmail.umd.edu",
    description="Simple ATM controller to acess bank account to deposit, withdraw and check the balance",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)