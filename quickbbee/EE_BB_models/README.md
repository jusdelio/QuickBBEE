The steps taken for the creation of the EE and BB models:

1. Firstly, we generated 100,000 parameters of dimension (100'000, 8) using [LatinHypercube](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.LatinHypercube.html#scipy.stats.qmc.LatinHypercube). Then, we used these parameters as inputs into [CAMB](https://camb.readthedocs.io/en/latest/) to generate spectra using the `get_lensed_scalar_cls` function.
   
2. Next, we prepared the obtained data by transforming them into dictionaries with the following format: for the parameters, keys are the names of each parameter, attributes are the corresponding columns for each parameter. For the spectra, keys are the multipoles and the features are the respective attributes, consisting of the interval concerned (starting from 2 because indices 0 and 1 are zero), and the spectra. We logged the values to facilitate computation using [cosmopower](https://github.com/alessiospuriomancini/cosmopower) (logging for prediction and delogging afterwards).



Here are the error graphs, for both the EE model, and the EE model:
![Capture d'écran 2024-05-24 15:06:47](https://github.com/jusdelio/QuickBBEE/assets/43094323/194d5d47-fde0-43d9-b575-4900d7fce1eb)
![Capture d'écran 2024-05-24 15:07:08](https://github.com/jusdelio/QuickBBEE/assets/43094323/b429c55c-f486-4a8e-82df-ab239be30471)
![Capture d'écran 2024-05-24 15:03:48](https://github.com/jusdelio/QuickBBEE/assets/43094323/dda1169c-f02d-4ce7-81a4-0189f4952e2f)
![Capture d'écran 2024-05-24 15:01:51](https://github.com/jusdelio/QuickBBEE/assets/43094323/1b17e6f4-f88f-433c-aa7d-adf4b6601322)


<div style="display: flex; flex-wrap: wrap;">
  <div style="flex: 1; padding: 10px;">
    <img src="https://github.com/jusdelio/QuickBBEE/assets/43094323/194d5d47-fde0-43d9-b575-4900d7fce1eb" style="width: 100%;">
  </div>
  <div style="flex: 1; padding: 10px;">
    <img src="https://github.com/jusdelio/QuickBBEE/assets/43094323/b429c55c-f486-4a8e-82df-ab239be30471" style="width: 100%;">
  </div>
  <div style="flex: 1; padding: 10px;">
    <img src="https://github.com/jusdelio/QuickBBEE/assets/43094323/dda1169c-f02d-4ce7-81a4-0189f4952e2f" style="width: 100%;">
  </div>
</div>
