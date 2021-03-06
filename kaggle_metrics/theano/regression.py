# Kaggle metrcis
# Krzysztof Joachimiak 2017

import theano
import theano.tensor as T
import warnings


# REGRESSION METRICS

# TODO: check input shapes

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

    return T.abs_(y_true - y_pred).mean()


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

    return (weights * T.abs_(y_true - y_pred)).mean()


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


    return T.sqrt(((y_true - y_pred)**2).mean())


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


    return T.sqrt(((T.log(y_pred + 1) - T.log(y_true + 1))**2).mean())
