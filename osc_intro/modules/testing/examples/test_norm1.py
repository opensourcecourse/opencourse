"""Exaple tests for norm"""

import numpy as np


def test_l2_norm_positive():
    random = np.random.random(100)
    assert np.linalg.norm(random, ord=2) > 0

def test_nan_returns_nan():
    random = np.random.random(100)
    random[10] = np.NaN
    out = np.linalg.norm(random)
    assert np.isnan(out)

