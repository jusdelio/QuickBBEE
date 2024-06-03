import pathlib
import setuptools

setuptools.setup(
    name="quickbbee",
    version="1.0.2",
    description="This package enables faster calculations of EE and BB spectra, leveraging models trained on data generated by CAMB.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Emmanuel Rasolofo, Giulio Ganci",
    license="GNU General Public License v3.0",
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research'
    ],
    install_requires=["cosmopower", "tf-keras"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    url="https://github.com/jusdelio/QuickBBEE.git" 
)
