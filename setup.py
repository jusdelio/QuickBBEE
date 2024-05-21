import pathlib
import setuptools

setuptools.setup(
    name="quickbbee",
    version="0.1.1",
    description="This package enables faster calculations of EE and BB spectra, leveraging models trained on data generated by CAMB.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Emmanuel Rasolofo, Giulio Ganci",
    license="The Unlicense",
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research'
    ],
    install_requires=["cosmopower"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    url="https://github.com/jusdelio/QuickBBEE.git" 
)
