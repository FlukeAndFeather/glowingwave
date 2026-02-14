#!/usr/bin/env python
"""
Script 04: Generate Figures

This script generates publication-quality figures from the analysis results.

Usage:
    python scripts/04_generate_figures.py
"""

import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Add src to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from src.data_utils import load_config
from src.plotting import setup_plotting_style, save_figure, plot_example


def main():
    """Generate figures from analysis results."""
    # Load configuration
    config = load_config('config.yaml')

    print("Starting figure generation...")

    # Set up plotting style
    setup_plotting_style(config)

    # Define paths
    processed_data_path = Path(config['data']['paths']['processed'])
    figures_path = Path(config['data']['paths']['figures'])

    # Ensure figures directory exists
    figures_path.mkdir(parents=True, exist_ok=True)

    # TODO: Update with your actual data file name
    # data_file = processed_data_path / 'processed_data.csv'

    # Load processed data
    # print(f"Loading processed data from {data_file}...")
    # data = pd.read_csv(data_file)

    # Generate figures
    # print("Generating Figure 1...")
    # fig1 = plot_example(data, config)
    # if config['plotting']['save_figures']:
    #     save_figure(fig1, 'figure_01', config)
    # plt.close(fig1)

    # Add more figures as needed
    # print("Generating Figure 2...")
    # fig2, ax = plt.subplots(figsize=tuple(config['plotting']['figsize']))
    # # Add your plotting code here
    # if config['plotting']['save_figures']:
    #     save_figure(fig2, 'figure_02', config)
    # plt.close(fig2)

    print("Figure generation complete!")
    print(f"Figures saved to: {figures_path}")


if __name__ == '__main__':
    main()
