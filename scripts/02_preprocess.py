#!/usr/bin/env python
"""
Script 02: Preprocess Data

This script cleans and preprocesses the raw data, saving the processed version.

Usage:
    python scripts/02_preprocess.py
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from src.data_utils import load_config, load_raw_data, clean_data, save_processed_data


def main():
    """Preprocess raw data."""
    # Load configuration
    config = load_config('config.yaml')

    print("Starting data preprocessing...")

    # Define paths
    raw_data_path = Path(config['data']['paths']['raw'])
    processed_data_path = Path(config['data']['paths']['processed'])

    # Ensure processed data directory exists
    processed_data_path.mkdir(parents=True, exist_ok=True)

    # TODO: Update with your actual data file name
    # raw_file = raw_data_path / 'your_data.csv'
    # processed_file = processed_data_path / 'processed_data.csv'

    # Load raw data
    # print(f"Loading raw data from {raw_file}...")
    # data = load_raw_data(raw_file)

    # Clean data
    # print("Cleaning data...")
    # data_clean = clean_data(data)

    # Save processed data
    # print(f"Saving processed data to {processed_file}...")
    # save_processed_data(data_clean, processed_file)

    print("Data preprocessing complete!")
    print(f"Processed data saved to: {processed_data_path}")


if __name__ == '__main__':
    main()
