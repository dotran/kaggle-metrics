# Kaggle metrcis
# Krzysztof Joachimiak 2017

import numpy as np
import warnings
from utils import check_shapes, align_shape


# REGRESSION METRICS

def mae(y_true, y_pred):

    '''

    Mean absolute error.

    Parameters
    ----------
    y_true: ndarray
        Ground truth
    y_pred: ndarray
        Array of predictions

    Returns
    -------
    rmsle: float
        Mean absolute error

    References
    ----------
    .. [1] https://www.kaggle.com/wiki/MeanAbsoluteError

    '''

    # Check shapes
    y_true, y_pred = align_shape(y_true, y_pred)
    check_shapes(y_true, y_pred)

    return np.abs(y_true - y_pred).mean()


def wmae(y_true, y_pred, weights):

    '''

    Weighted mean absolute error.

    Parameters
    ----------
    y_true: ndarray
        Ground truth
    y_pred: ndarray
        Array of predictions

    Returns
    -------
    rmsle: float
        Weighted mean absolute error

    References
    ----------
    .. [1] https://www.kaggle.com/wiki/WeightedMeanAbsoluteError

    '''

    # Check shapes
    y_true, y_pred = align_shape(y_true, y_pred)
    check_shapes(y_true, y_pred)

    return (weights * np.abs(y_true - y_pred)).mean()


def rmse(y_true, y_pred):
    '''

    Root mean squared error.

    Parameters
    ----------
    y_true: ndarray
        Ground truth
    y_pred: ndarray
        Array of predictions

    Returns
    -------
    rmsle: float
        Root mean squared error

    References
    ----------
    .. [1] https://www.kaggle.com/wiki/RootMeanSquaredError

    '''

    # Check shapes
    y_true, y_pred = align_shape(y_true, y_pred)
    check_shapes(y_true, y_pred)

    return np.sqrt(((y_true - y_pred)**2).mean())


def rmsle(y_true, y_pred):
    '''

    Root mean squared logarithmic error.

    Parameters
    ----------
    y_true: ndarray
        Ground truth
    y_pred: ndarray
        Array of predictions

    Returns
    -------
    rmsle: float
        Root mean squared logarithmic error

    References
    ----------
    .. [1] https://www.kaggle.com/wiki/RootMeanSquaredLogarithmicError
    .. [2] https://www.slideshare.net/KhorSoonHin/rmsle-cost-function

    '''

    # Check shapes
    y_true, y_pred = align_shape(y_true, y_pred)
    check_shapes(y_true, y_pred)

    return np.sqrt(((np.log(y_pred + 1) - np.log(y_true + 1))**2).mean())

def ae():
    pass
