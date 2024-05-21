# QuickBBEE 

# Installation

We recommend installing [bbee.py](bbee.py) within a [Conda](https://docs.conda.io/projects/conda/en/latest/index.html) virtual environment. 
For example, to create and activate an environment called ``cp_env``, use:

    conda create -n cp_env python=3.7 pip && conda activate cp_env

Once inside the environment, you can install [bbee.py](bbee.py):

- **from PyPI** 

        pip install quickbbee

    To test the installation, you can use

        python3 -c 'import quickbbee as quick'


- **from source**

        git clone https://github.com/jusdelio/QuickBBEE
        cd quickbbee
        pip install -e .

    To test the installation, you can use

        pytest

If you are interested in how we trained the two models, follow this [link](https://github.com/jusdelio/QuickBBEE/blob/main/quickbbee/EE_BB_models/README.md) 
