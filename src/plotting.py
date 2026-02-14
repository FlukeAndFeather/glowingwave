"""
Plotting and visualization utilities.

This module contains functions for creating publication-quality figures.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def setup_plotting_style(config=None):
    """
    Set up matplotlib/seaborn plotting style.

    Parameters
    ----------
    config : dict, optional
        Configuration dictionary with plotting parameters
    """
    if config is None:
        config = {}

    plotting_config = config.get('plotting', {})

    # Set style
    style = plotting_config.get('style', 'seaborn-v0_8-darkgrid')
    try:
        plt.style.use(style)
    except:
        plt.style.use('default')

    # Set seaborn defaults
    sns.set_context("paper")
    sns.set_palette(plotting_config.get('palette', 'Set2'))


def save_figure(fig, filename, config=None, **kwargs):
    """
    Save figure with consistent settings.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure to save
    filename : str or Path
        Output filename
    config : dict, optional
        Configuration dictionary
    **kwargs
        Additional arguments passed to fig.savefig()
    """
    if config is None:
        config = {}

    plotting_config = config.get('plotting', {})
    data_config = config.get('data', {})

    # Get output directory
    figures_dir = Path(data_config.get('paths', {}).get('figures', 'figures'))
    figures_dir.mkdir(exist_ok=True)

    # Get format and dpi
    fmt = plotting_config.get('format', 'png')
    dpi = plotting_config.get('dpi', 300)

    # Construct full path
    filepath = figures_dir / f"{filename}.{fmt}"

    # Save
    fig.savefig(filepath, dpi=dpi, bbox_inches='tight', **kwargs)
    print(f"Figure saved to: {filepath}")


def plot_example(data, config=None):
    """
    Example plotting function.

    Parameters
    ----------
    data : pd.DataFrame or array-like
        Data to plot
    config : dict, optional
        Configuration dictionary

    Returns
    -------
    matplotlib.figure.Figure
        Created figure
    """
    if config is None:
        config = {}

    plotting_config = config.get('plotting', {})
    figsize = tuple(plotting_config.get('figsize', [10, 6]))

    fig, ax = plt.subplots(figsize=figsize)

    # Add your plotting code here
    # Example: ax.plot(data)

    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    ax.set_title("Plot Title")

    return fig
