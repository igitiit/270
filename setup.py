from setuptools import setup, find_packages

setup(
    name="bank_system",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest>=7.4.3",
        "pytest-cov>=4.1.0",
    ],
    python_requires=">=3.9",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple bank account management system",
    keywords="banking, finance, accounts",
)
