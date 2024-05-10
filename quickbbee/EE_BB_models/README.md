This directory contains the "QuickBBEE" package.

- [bbee.py](bbee.py) contains two classes:
  - `set_dparams`: Initializes an object to generate two spectra EE and BB using provided models.
  - `set_cparams`: Initializes an object allowing the user to specify their own model created only by [cosmopower](https://github.com/alessiospuriomancini/cosmopower/blob/main/cosmopower).

The steps taken for the creation of the EE and BB models:

1. Firstly, we generated 100,000 parameters of dimension (100,000, 8) using [LatinHypercube](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.LatinHypercube.html#scipy.stats.qmc.LatinHypercube). Then, we used these parameters as inputs into [CAMB](https://camb.readthedocs.io/en/latest/) to generate spectra using the `get_lensed_scalar_cls` function.
   
2. Next, we prepared the obtained data by transforming them into dictionaries with the following format: for the parameters, keys are the names of each parameter, attributes are the corresponding columns for each parameter. For the spectra, keys are the multipoles and the features are the respective attributes, consisting of the interval concerned (starting from 2 because indices 0 and 1 are zero), and the spectra. For the EE spectra, we logged the values to facilitate computation using [cosmopower](https://github.com/alessiospuriomancini/cosmopower) (logging for prediction and delogging afterwards). For the BB spectra, on the other hand, we used PCA compression, a method aimed at simplifying data while preserving their structure and essential characteristics.

After training the data, the error committed by the two models is shown below.
