"""
Analysis functions.

This module contains functions for statistical analysis and modeling.
"""

import numpy as np
import pandas as pd
from scipy import stats


def compute_summary_statistics(data, columns=None):
    """
    Compute summary statistics for data.

    Parameters
    ----------
    data : pd.DataFrame
        Input data
    columns : list, optional
        Specific columns to analyze. If None, analyze all numeric columns.

    Returns
    -------
    pd.DataFrame
        Summary statistics
    """
    if columns is None:
        # Select only numeric columns
        data = data.select_dtypes(include=[np.number])
    else:
        data = data[columns]

    return data.describe()


def example_analysis(data, **params):
    """
    Example analysis function.

    Parameters
    ----------
    data : pd.DataFrame or array-like
        Input data
    **params
        Analysis parameters

    Returns
    -------
    dict
        Analysis results
    """
    # Implement your analysis logic
    results = {
        'mean': np.mean(data),
        'std': np.std(data),
        # Add more results as needed
    }

    return results


def statistical_test(group1, group2, test='ttest'):
    """
    Perform statistical test comparing two groups.

    Parameters
    ----------
    group1 : array-like
        First group
    group2 : array-like
        Second group
    test : str
        Type of test ('ttest', 'mannwhitney', etc.)

    Returns
    -------
    dict
        Test results including statistic and p-value
    """
    if test == 'ttest':
        statistic, pvalue = stats.ttest_ind(group1, group2)
    elif test == 'mannwhitney':
        statistic, pvalue = stats.mannwhitneyu(group1, group2)
    else:
        raise ValueError(f"Unknown test: {test}")

    return {
        'statistic': statistic,
        'pvalue': pvalue,
        'test': test
    }
