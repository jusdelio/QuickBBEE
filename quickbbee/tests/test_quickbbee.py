import math
import numpy as np
from quickbbee import set_dparams, set_cparams
import pytest


H0, Alens, r, tau, ns, As, ombh2, omch2 = 68, 0.2, 0.02, 0.035, 0.97, math.exp(3.3)*10**-10, 0.020, 0.05
ranges = np.array([[65, 75],
                   [0, 1],
                   [0, 0.5],
                   [0.03, 0.09],
                   [0.94, 0.99],
                   [math.exp(3.0)*10**-10, math.exp(3.5)*10**-10],
                   [0.02, 0.025],
                   [0.05, 0.3]])

def test_ranges():
    model = set_dparams(H0, Alens, r, tau, ns, As, ombh2, omch2, 2400)
    interval = model.get_params_interval()
    assert np.allclose(interval, ranges)

def test_set_cparams():
    model = set_cparams(H0, Alens, r, tau, ns, As, ombh2, omch2, '../EE_BB__models/cp_NN_BB', ranges, True ,False,2400)
    interval = model.get_params_interval()
    assert np.allclose(interval, ranges)


