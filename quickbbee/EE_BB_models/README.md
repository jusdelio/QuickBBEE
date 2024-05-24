The steps taken for the creation of the EE and BB models:

1. Firstly, we generated 100,000 parameters of dimension (100'000, 8) using [LatinHypercube](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.LatinHypercube.html#scipy.stats.qmc.LatinHypercube). Then, we used these parameters as inputs into [CAMB](https://camb.readthedocs.io/en/latest/) to generate spectra using the `get_lensed_scalar_cls` function.
   
2. Next, we prepared the obtained data by transforming them into dictionaries with the following format: for the parameters, keys are the names of each parameter, attributes are the corresponding columns for each parameter. For the spectra, keys are the multipoles and the features are the respective attributes, consisting of the interval concerned (starting from 2 because indices 0 and 1 are zero), and the spectra. We logged the values to facilitate computation using [cosmopower](https://github.com/alessiospuriomancini/cosmopower) (logging for prediction and delogging afterwards).




![Capture d'écran 2024-05-17 16:03:24](https://github.com/jusdelio/QuickBBEE/assets/43094323/2ae7c078-f861-426f-ac29-30556d442ba5)
![Capture d'écran 2024-05-06 14:06:59](https://github.com/jusdelio/QuickBBEE/assets/43094323/6222fca4-3af9-4842-a49e-86cd875572e8)
