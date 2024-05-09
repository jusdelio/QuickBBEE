# QuickBBEE (Beta)

# Installation

We recommend installing [bbee.py](bbee.py) within a [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) virtual environment. 
For example, to create and activate an environment called ``cp_env``, use:

    conda create -n cp_env python=3.7 pip && conda activate cp_env

Once inside the environment, you can install [bbee.py](bbee.py):

- **from PyPI**

        pip install quickbbee

    To test the installation, you can use

        python3 -c 'import quickbbee as quick'
    
    If you do not have a GPU on your machine, you will see a warning message about it which you can safely ignore.

- **from source**

        git clone https://github.com/jusdelio/QuickBBEE
        cd quickbbee
        pip install -e .

    To test the installation, you can use

        pytest


## Generate Spectra

the first step is to initialize the parameters with the wanted values:

```python
from quickbbee import set_dparams
from quickbbee import set_cparams
import matplotlib.pyplot as plt
import math as m
import numpy as np

H0, Alens, r, tau, ns, As, ombh2, omch2 = 68, 0.2, 0.02, 0.035, 0.97, m.exp(3.3)*10**-10, 0.020, 0.05
```

Then, we create a class (model) with the wanted parameters :

```python
l_max = 2400

model = set_dparams(H0, Alens, r, tau, ns, As, ombh2, omch2, lmax)
```


## Default Parameter Intervals

| Parameter | Interval                |
|-----------|-------------------------|
| H0        | [65, 75]                |
| Alens     | [0, 1]                  |
| r         | [0, 0.5]                |
| tau       | [0.03, 0.09]            |
| ns        | [0.94, 0.99]            |
| As        | [exp(3.0)*10^-10, exp(3.5)*10^-10] |
| ombh2     | [0.02, 0.025]           |
| omch2     | [0.05, 0.30]           |

This table represents the default intervals used by the models in `set_dparams`.
Example:

```python
H0, Alens, r, tau, ns, As, ombh2, omch2 = 68, 0.2, 0.02, 0.035, 0.97, m.exp(3.3)*10**-10, 0.020, 0.05
model = set_dparams(H0, Alens, r, tau, ns, As, ombh2, omch2, 2400)
interval = model.get_params_interval()
```


## Output
```python
Intervals:
H0: [65. 75.]
Alens: [0. 1.]
r: [0.  0.5]
tau: [0.03 0.09]
ns: [0.94 0.99]
As: [2.00855369e-09 3.31154520e-09]
ombh2: [0.02  0.025]
omch2: [0.05 0.3]
```
